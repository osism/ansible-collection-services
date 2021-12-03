# -*- coding: utf-8 -*-
#
# Copyright 2019 Radosław Piliszek (yoctozepto)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from jinja2.filters import contextfilter
from jinja2.runtime import Undefined

try:
    from ansible.errors import AnsibleFilterError
except ImportError:
    # NOTE(mgoddard): For unit testing we don't depend on Ansible since it is
    # not in global requirements.
    AnsibleFilterError = Exception


class FilterError(AnsibleFilterError):
    """Error during execution of a jinja2 filter."""


def _call_bool_filter(context, value):
    """Pass a value through the 'bool' filter.

    :param context: Jinja2 Context object.
    :param value: Value to pass through bool filter.
    :returns: A boolean.
    """
    return context.environment.call_filter("bool", value, context=context)


@contextfilter
def kolla_address(context, network_name, hostname=None):
    """returns IP address on the requested network

    The output is affected by '<network_name>_*' variables:
    '<network_name>_interface' sets the interface to obtain address for.
    '<network_name>_address_family' controls the address family (ipv4/ipv6).

    :param context: Jinja2 Context
    :param network_name: string denoting the name of the network to get IP
                         address for, e.g. 'api'
    :param hostname: to override host which address is retrieved for
    :returns: string with IP address
    """

    # NOTE(yoctozepto): watch out as Jinja2 'context' behaves not exactly like
    # the python 'dict' (but mimics it most of the time)
    # for example it returns a special object of type 'Undefined' instead of
    # 'None' or value specified as default for 'get' method
    # 'HostVars' shares this behavior

    if hostname is None:
        hostname = context.get('inventory_hostname')
        if isinstance(hostname, Undefined):
            raise FilterError("'inventory_hostname' variable is unavailable")

    hostvars = context.get('hostvars')
    if isinstance(hostvars, Undefined):
        raise FilterError("'hostvars' variable is unavailable")

    # NOTE: The kolla_address filter is used in osism-ansible to read the
    # facts from a host. If in the first step of generic-write-facts.yml
    # when creating the template for a host the hostvars are not present in
    # the context, the content is simply returned as it was before applying
    # the filter.

    if not hostvars and not hostname:
        return "{{ '%s' | kolla_address(host) }}" % network_name
    if not hostvars:
        return "{{ '%s' | kolla_address }}" % network_name

    host = hostvars.get(hostname)
    if isinstance(host, Undefined):
        raise FilterError("'{hostname}' not in 'hostvars'"
                          .format(hostname=hostname))

    del hostvars  # remove for clarity (no need for other hosts)

    # NOTE(yoctozepto): variable "host" will *not* return Undefined
    # same applies to all its children (act like plain dictionary)

    interface_name = host.get(network_name + '_interface')
    if interface_name is None:
        raise FilterError("Interface name undefined "
                          "for network '{network_name}' "
                          "(set '{network_name}_interface')"
                          .format(network_name=network_name))

    address_family = host.get(network_name + '_address_family')
    if address_family is None:
        raise FilterError("Address family undefined "
                          "for network '{network_name}' "
                          "(set '{network_name}_address_family')"
                          .format(network_name=network_name))
    address_family = address_family.lower()
    if address_family not in ['ipv4', 'ipv6']:
        raise FilterError("Unknown address family '{address_family}' "
                          "for network '{network_name}'"
                          .format(address_family=address_family,
                                  network_name=network_name))

    ansible_interface_name = interface_name.replace('-', '_')
    interface = host.get('ansible_' + ansible_interface_name)
    if interface is None:

        # NOTE: The kolla_address filter is used in osism-ansible to
        #       read the facts from a host. If a single interface is
        # not yet present on a host, that is fine in that case.

        # raise FilterError("Interface '{interface_name}' "
        #                   "not present "
        #                   "on host '{hostname}'"
        #                   .format(interface_name=interface_name,
        #                           hostname=hostname))

        return ""

    af_interface = interface.get(address_family)
    if af_interface is None:
        raise FilterError("Address family '{address_family}' undefined "
                          "on interface '{interface_name}' "
                          "for host: '{hostname}'"
                          .format(address_family=address_family,
                                  interface_name=interface_name,
                                  hostname=hostname))

    if address_family == 'ipv4':
        address = af_interface.get('address')
    elif address_family == 'ipv6':
        # ipv6 has no concept of a secondary address
        # explicitly exclude the vip addresses
        # to avoid excluding all /128

        haproxy_enabled = host.get('enable_haproxy')
        if haproxy_enabled is None:
            raise FilterError("'enable_haproxy' variable is unavailable")
        haproxy_enabled = _call_bool_filter(context, haproxy_enabled)

        if haproxy_enabled:
            vip_addresses = [
                host.get('kolla_internal_vip_address'),
                host.get('kolla_external_vip_address'),
            ]
        else:
            # no addresses are virtual (kolla-wise)
            vip_addresses = []

        global_ipv6_addresses = [x for x in af_interface if
                                 x['scope'] == 'global' and
                                 x['address'] not in vip_addresses]

        if global_ipv6_addresses:
            address = global_ipv6_addresses[0]['address']
        else:
            address = None

    if address is None:
        raise FilterError("{address_family} address missing "
                          "on interface '{interface_name}' "
                          "for host '{hostname}'"
                          .format(address_family=address_family,
                                  interface_name=interface_name,
                                  hostname=hostname))

    return address


def put_address_in_context(address, context):
    """puts address in context

    :param address: the address to contextify
    :param context: describes context in which the address appears,
                    either 'url' or 'memcache',
                    affects only IPv6 addresses format
    :returns: string with address in proper context
    """

    if context not in ['url', 'memcache']:
        raise FilterError("Unknown context '{context}'"
                          .format(context=context))

    if ':' not in address:
        return address

    # must be IPv6 raw address

    if context == 'url':
        return '[{address}]'.format(address=address)
    elif context == 'memcache':
        return 'inet6:[{address}]'.format(address=address)

    return address


class FilterModule(object):
    """IP address filters"""

    def filters(self):
        return {
            'kolla_address': kolla_address,
            'put_address_in_context': put_address_in_context,
        }
