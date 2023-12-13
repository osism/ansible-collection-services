from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_tuned_package_installed(host):
    tuned_package_name = get_variable(host, "tuned_package_name")
    tuned_package = host.package(tuned_package_name)
    assert (
        tuned_package.is_installed
    ), f"Package {tuned_package_name} should be installed"


def test_tuned_service_running_and_enabled(host):
    tuned_service_name = get_variable(host, "tuned_service_name")
    tuned_service = host.service(tuned_service_name)
    assert tuned_service.is_running, f"Service {tuned_service_name} should be running"
    assert tuned_service.is_enabled, f"Service {tuned_service_name} should be enabled"


def test_tuned_profile_set_correctly(host):
    tuned_profile = get_variable(host, "tuned_profile")
    # Execute the command to get the active tuned profile
    result = host.check_output("tuned-adm active | awk -F': ' '{print $2}'")
    assert (
        result == tuned_profile
    ), f"The active tuned profile should be {tuned_profile}, but found {result}"
