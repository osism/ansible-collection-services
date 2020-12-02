# https://www.openpolicyagent.org/docs/latest/docker-authorization/
# https://github.com/open-policy-agent/opa-docker-authz

package docker.authz

default allow = false

allow {
    not deny
}

deny {
    unknown_image_registry
}

unknown_image_registry {
    splitted := split(input.Body.Image, "/")
    not startswith(input.Body.Image, "index.docker.io");
    not startswith(input.Body.Image, "quay.io");
    count(splitted) > 2
}
