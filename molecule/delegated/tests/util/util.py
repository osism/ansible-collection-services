import os
import urllib.request
import testinfra.utils.ansible_runner


def get_ansible():
    testinfra_runner = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]
    )
    testinfra_hosts = testinfra_runner.get_hosts("all")

    return testinfra_runner, testinfra_hosts


def get_variable(host, name, fact=False):
    if fact:
        ansible_facts = host.ansible("setup")["ansible_facts"]

        if name not in ansible_facts:
            raise Exception(f"Fact {name} not found!")

        return ansible_facts[name]

    all_vars = host.ansible.get_variables()
    if name in all_vars:
        return all_vars[name]

    # debug_value = host.ansible("debug", f"var={name}")[name]
    # if type(debug_value) is str and not debug_value.startswith('VARIABLE IS NOT DEFINED!'):
    #    return debug_value
    # elif type(debug_value) is dict:
    #    return debug_value

    role_name = os.environ["ROLE_NAME"]

    test_vars = host.ansible(
        "include_vars", f"../../molecule/delegated/vars/{role_name}.yml"
    )["ansible_facts"]
    if name in test_vars:
        return test_vars[name]

    default_vars = host.ansible(
        "include_vars", f"../../roles/{role_name}/defaults/main.yml"
    )["ansible_facts"]
    if name in default_vars:
        return default_vars[name]

    raise Exception(f"Variable {name} not found!")


def get_os_role_variable(host, name, filename=None):
    role_name = os.environ["ROLE_NAME"]

    if filename is None:
        filename = get_variable(host, "ansible_os_family", True) + ".yml"

    path = f"../../roles/{role_name}/vars/{filename}"
    variables = host.ansible("include_vars", path)["ansible_facts"]

    if name not in variables:
        raise Exception(f"{name} not found in {path}")

    return variables[name]


def get_from_url(url, binary=False):
    resource = urllib.request.urlopen(url)

    if not binary:
        encoding = resource.headers.get_content_charset()
        if encoding is None:
            encoding = "utf-8"
        content = resource.read().decode(encoding)
    else:
        content = resource.read()

    return content


def jinja_replacement(original_variable, replacements):
    original_variable = original_variable.replace("{{ ", "{").replace(" }}", "}")
    original_variable = original_variable.format(**replacements)

    return original_variable


def jinja_list_concat(original_variable, lists):
    if type(original_variable) is list:
        return original_variable

    return_value = []
    for li in lists:
        return_value += li

    return return_value
