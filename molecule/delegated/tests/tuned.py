from .util.util import get_ansible, get_variable, get_dist_role_variable

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
    tuned_profile = get_dist_role_variable(host, "tuned_profile")

    # Check if 'tuned-adm' is available and capture the output
    tuned_adm_check = host.run("which tuned-adm")

    # Fail the test if 'tuned-adm' is not found, including the command output
    assert tuned_adm_check.rc == 0, f"'tuned-adm' command not found. Output: {tuned_adm_check.stdout or tuned_adm_check.stderr}"

    # Execute the command to get the active tuned profile
    result = host.check_output("tuned-adm active | awk -F': ' '{print $2}'")

    # Include the output of 'which tuned-adm' in the assert message
    assert (
        result == tuned_profile
    ), f"The active tuned profile should be {tuned_profile}, but found {result}. 'which tuned-adm' output: {tuned_adm_check.stdout or tuned_adm_check.stderr}"

