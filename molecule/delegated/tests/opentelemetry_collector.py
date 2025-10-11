from .util.util import get_ansible, get_variable

testinfra_runner, testinfra_hosts = get_ansible()


def test_opentelemetry_collector_directories(host):
    """Test that all required directories exist with correct permissions."""
    directories = [
        get_variable(host, "opentelemetry_collector_configuration_directory"),
        get_variable(host, "opentelemetry_collector_data_directory"),
        get_variable(host, "opentelemetry_collector_docker_compose_directory"),
    ]
    for directory in directories:
        dir = host.file(directory)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == get_variable(host, "operator_user")
        assert dir.group == get_variable(host, "operator_group")
        assert dir.mode == 0o750


def test_docker_compose_file(host):
    """Test that docker-compose.yml exists with correct permissions."""
    docker_compose_file_path = f"{get_variable(host, 'opentelemetry_collector_docker_compose_directory')}/docker-compose.yml"  # noqa: E501
    docker_compose_file = host.file(docker_compose_file_path)
    assert docker_compose_file.exists
    assert not docker_compose_file.is_directory
    assert docker_compose_file.user == get_variable(host, "operator_user")
    assert docker_compose_file.group == get_variable(host, "operator_group")
    assert docker_compose_file.mode == 0o640


def test_otel_collector_config_file(host):
    """Test that OTel collector config exists with correct permissions."""
    config_file_path = f"{get_variable(host, 'opentelemetry_collector_configuration_directory')}/otel-collector-config.yml"  # noqa: E501
    config_file = host.file(config_file_path)
    assert config_file.exists
    assert not config_file.is_directory
    assert config_file.user == get_variable(host, "operator_user")
    assert config_file.group == get_variable(host, "operator_group")
    assert config_file.mode == 0o644


def test_opentelemetry_collector_service(host):
    """Test that the service is running and enabled."""
    service = host.service(get_variable(host, "opentelemetry_collector_service_name"))
    assert service.is_running
    assert service.is_enabled


def test_otel_config_content(host):
    """Test that OTel config contains required sections."""
    config_file_path = f"{get_variable(host, 'opentelemetry_collector_configuration_directory')}/otel-collector-config.yml"  # noqa: E501
    config_file = host.file(config_file_path)
    content = config_file.content_string

    # Verify main sections exist
    assert "receivers:" in content
    assert "prometheus:" in content
    assert "otlp:" in content  # OTLP receiver
    assert "exporters:" in content
    assert "otlp:" in content  # OTLP exporter
    assert "debug:" in content  # Debug exporter (replaced logging)
    assert "service:" in content
    assert "pipelines:" in content
    assert "metrics:" in content
    assert "logs:" in content  # Logs pipeline added


def test_otel_collector_container_running(host):
    """Test that the OpenTelemetry Collector container is running."""
    container_name = get_variable(host, "opentelemetry_collector_container_name")

    # Check if container exists and is running
    container_check = host.run(
        f"docker ps --filter name={container_name} --format '{{{{.Names}}}}'"
    )
    assert container_name in container_check.stdout


def test_otel_config_prometheus_scrape(host):
    """Test that Prometheus scrape configuration is present in OTel config."""
    config_file_path = f"{get_variable(host, 'opentelemetry_collector_configuration_directory')}/otel-collector-config.yml"  # noqa: E501
    config_file = host.file(config_file_path)
    content = config_file.content_string

    # Verify Prometheus receiver configuration
    assert "prometheus:" in content
    assert "config:" in content
    assert "scrape_configs:" in content


def test_otel_config_dash0_exporter(host):
    """Test that Dash0 OTLP exporter configuration is present in OTel config."""
    config_file_path = f"{get_variable(host, 'opentelemetry_collector_configuration_directory')}/otel-collector-config.yml"  # noqa: E501
    config_file = host.file(config_file_path)
    content = config_file.content_string

    # Verify OTLP exporter configuration for Dash0
    assert "otlp:" in content
    assert "endpoint:" in content
    # Note: We don't check for the actual token value for security reasons


def test_otel_config_otlp_receiver(host):
    """Test that OTLP receiver configuration is present in OTel config."""
    config_file_path = f"{get_variable(host, 'opentelemetry_collector_configuration_directory')}/otel-collector-config.yml"  # noqa: E501
    config_file = host.file(config_file_path)
    content = config_file.content_string

    # Verify OTLP receiver configuration
    assert "otlp:" in content
    assert "protocols:" in content
    assert "grpc:" in content
    assert "http:" in content
    assert "4317" in content  # gRPC port
    assert "4318" in content  # HTTP port


def test_otel_config_logs_pipeline(host):
    """Test that logs pipeline configuration is present in OTel config."""
    config_file_path = f"{get_variable(host, 'opentelemetry_collector_configuration_directory')}/otel-collector-config.yml"  # noqa: E501
    config_file = host.file(config_file_path)
    content = config_file.content_string

    # Verify logs pipeline exists
    assert "logs:" in content
    assert "receivers:" in content
    # Logs pipeline should use OTLP receiver
    # Note: We check for the general structure, actual receiver list is in YAML format
