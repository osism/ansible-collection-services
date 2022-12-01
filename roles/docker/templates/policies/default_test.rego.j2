# https://www.openpolicyagent.org/docs/latest/policy-testing/

package docker.authz

test_registry_quay_allowed {
    allow with input as {"Body": {"Image": "quay.io/osism/template:latest"}}
}

test_registry_dockerhub_allowd {
    allow with input as {"Body": {"Image": "index.docker.io/osism/template:latest"}}
}

test_registry_default_allowed {
    allow with input as {"Body": {"Image": "osism/template:latest"}}
}

test_registry_other_denied {
    not allow with input as {"Body": {"Image": "docker.pkg.github.com/osism/template:latest"}}
}

test_image_invalid_name_denied {
    not allow with input as {"Body": {"Image": "foo/bar/osism/template:latest"}}
}

test_image_library_allowed {
    allow with input as {"Body": {"Image": "python:latest"}}
}
