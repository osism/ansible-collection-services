from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_netdata_package_installed(host):
    package_name = get_variable(host, "netdata_package_name")
    package = host.package(package_name)
    assert package.is_installed


def test_repository_configuration(host):
    if get_variable(host, "netdata_configure_repository"):
        repo_key_url = get_variable(host, "netdata_debian_repository_key")
        repo = get_variable(host, "netdata_debian_repository")
        debian_version = host.system_info.distribution_version

        if debian_version < "22.04":
            assert host.run(f"apt-key list | grep {repo_key_url}").rc == 0
        else:
            gpg_key_file = "/etc/apt/trusted.gpg.d/netdata.asc"
            assert host.file(gpg_key_file).exists

        assert host.run(f"apt-cache policy | grep {repo.split(' ')[1]}").rc == 0


def test_netdata_configuration_files(host):
    configuration_files = get_variable(host, "netdata_configuration_files")
    for file in configuration_files:
        config_file = host.file(f"/etc/netdata/{file}")
        assert config_file.exists
        assert config_file.user == "root"
        assert config_file.group == "root"
        assert config_file.mode == 0o644


def test_directories_and_files(host):
    cloud_dir = host.file("/var/lib/netdata/cloud.d")
    opt_out_file = host.file("/etc/netdata/.opt-out-from-anonymous-statistics")

    assert cloud_dir.exists
    assert cloud_dir.is_directory
    assert cloud_dir.user == "netdata"
    assert cloud_dir.group == "netdata"
    assert cloud_dir.mode == 0o775

    assert not opt_out_file.exists or (
            opt_out_file.user == "root" and opt_out_file.group == "root"
    )


def test_netdata_user_group(host):
    netdata_user = host.user("netdata")
    assert "docker" in netdata_user.groups


def test_netdata_service_running(host):
    service = host.service(get_variable(host, "netdata_service_name"))
    assert service.is_running
    assert service.is_enabled

# Commented out as include in Role (tasks/main.yml) is missing for server.yml
# def test_netdata_sysctl_setting(host):
#    sysctl_file_path = "/etc/sysctl.d/50-netdata.conf"
#    assert host.file(sysctl_file_path).exists

#    netdata_vm_max_map_count = get_variable(host, "netdata_sys_vm_max_map_count")
#    expected_value = str(netdata_vm_max_map_count)
#    actual_value = host.sysctl("vm.max_map_count")

#    assert actual_value == expected_value
