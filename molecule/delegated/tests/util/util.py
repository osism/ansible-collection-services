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


def get_role_variable(host, name, filename):
    role_name = os.environ["ROLE_NAME"]

    path = f"../../roles/{role_name}/vars/{filename}"
    variables = host.ansible("include_vars", path)["ansible_facts"]

    if name not in variables:
        raise Exception(f"{name} not found in {path}")

    return variables[name]


def get_family_role_variable(host, name):
    return get_role_variable(
        host, name, get_variable(host, "ansible_os_family", True) + "-family.yml"
    )


def get_dist_role_variable(host, name):
    return get_role_variable(
        host, name, get_variable(host, "ansible_distribution", True) + "-dist.yml"
    )


def get_from_url(url, binary=False):
    # Create a request object with a faked User-Agent header, some websites like https://pkg.osquery.io/rpm/GPG
    # Will need this, otherwise they will return http 403 forbidden
    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0 (Linux x86_64) Chrome/103.0.0.0"}
    )
    # Open the URL with the custom request object
    resource = urllib.request.urlopen(req)

    if not binary:
        encoding = resource.headers.get_content_charset()
        if encoding is None:
            encoding = "utf-8"
        content = resource.read().decode(encoding)
    else:
        content = resource.read()

    return content


def get_centos_repo_key(host, summary):
    all_keys = host.run("rpm -qa gpg-pubkey | xargs -I{} sh -c 'rpm -qi {}'").stdout
    split_on = "{}\nDescription :\n-----BEGIN PGP PUBLIC KEY BLOCK-----\n".format(
        summary
    )
    installed_key = all_keys.split(split_on)[1].split(
        "-----END PGP PUBLIC KEY BLOCK-----"
    )[0]
    installed_key = "\n".join(installed_key.split("\n")[2:])

    return installed_key


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
