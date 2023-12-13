from .util.util import (
    get_ansible,
    get_variable,
    get_os_role_variable,
    jinja_replacement,
    jinja_list_concat,
)

testinfra_runner, testinfra_hosts = get_ansible()


def test_pkg(host):
    package_name = get_variable(host, "auditd_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed

    package_name = get_variable(host, "audispd_plugins_package_name")
    assert package_name != ""

    package = host.package(package_name)
    assert package.is_installed


def test_conffile(host):
    f = host.file("/etc/audit")
    assert f.exists
    assert f.is_directory

    with host.sudo("root"):
        actual_content = host.check_output("cat /etc/audit/audit.conf")
        assert actual_content.strip() != ""
        assert (
            "This file controls the configuration of the audit daemon" in actual_content
        )


def test_adjustment(host):
    auditd_config = get_variable(host, "auditd_config")

    auditd_plugin_path = get_variable(host, "auditd_plugin_path")
    if (
        host.system_info.distribution.lower() == "ubuntu"
        and host.system_info.codename.lower() == "jammy"
    ):
        auditd_plugin_path = get_os_role_variable(
            host, "auditd_plugin_path", "jammy.yml"
        )

    for config in auditd_config:
        parameter = config["parameter"]
        path = config["config"]
        path = jinja_replacement(path, {"auditd_plugin_path": auditd_plugin_path})

        with host.sudo("root"):
            actual_content = host.check_output(f"cat {path}")
            assert actual_content.strip() != ""
            assert f"{parameter} =" in actual_content


def test_rulefiles(host):
    auditd_rules_files = get_variable(host, "auditd_rules_files")
    auditd_rules_files_defaults = get_variable(host, "auditd_rules_files_defaults")
    auditd_rules_files_extra = get_variable(host, "auditd_rules_files_extra")

    auditd_rules_files = jinja_list_concat(
        auditd_rules_files, [auditd_rules_files_defaults, auditd_rules_files_extra]
    )

    auditd_rules_path = get_variable(host, "auditd_rules_path")

    managed_files = set()

    for item in auditd_rules_files:
        path = f"{auditd_rules_path}/{item}"

        with host.sudo("root"):
            actual_content = host.check_output(f"cat {path}")
            assert actual_content.strip() != ""

        managed_files.add(f"{item}")

    file_set = set()
    with host.sudo("root"):
        file_set = set(host.file(f"{auditd_rules_path}").listdir())

    managed_difference = file_set - managed_files

    assert len(managed_difference) == 0 or (
        len(managed_difference) == 1 and "osas-auditd-rhel7.rules" in managed_difference
    )


def test_srv(host):
    service = host.service(get_variable(host, "auditd_service_name"))

    assert service.is_running
    assert service.is_enabled
