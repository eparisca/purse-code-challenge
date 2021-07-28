#!/usr/bin/env bash

set -x
set -euo pipefail

########################################
# @return string
########################################
function usage() {
    echo "
NAME ${0} -- Build, tag, and push a container image
SYNOPSIS
    ${0} APP_VERSION
EXAMPLES
    ${0} 1.0.0
"
}

wd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

namespace="eparisca"
app_name="$(basename $(git rev-parse --show-toplevel))"
app_version="${1}"
package="${app_name}-${app_version}"
image_name="${app_name}:${app_version}"

app_description="Purse Code Challenge"

docker build . \
    --label maintainer="Emilio Parisca <eparisca@gmail.com>" \
    --label org.label-schema.build-date=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
    --label org.label-schema.name="${namespace}/${app_name}" \
    --label org.label-schema.version="${app_version}" \
    --label org.label-schema.description="${app_description}" \
    --label org.label-schema.vcs-url="https://github.com/${namespace}/${app_name}" \
    --build-arg APP_NAME="${app_name}" \
    -t "${image_name}"
