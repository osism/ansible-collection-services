from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_base_config_dir(host):
    dir = host.file(get_variable(host, "zuul_base_conf_dir"))
    assert dir.exists
    assert dir.is_directory
    assert dir.user == get_variable(host, "operator_user")
    assert dir.group == get_variable(host, "operator_group")
    assert dir.mode == 0o755
