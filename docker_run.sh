#!/usr/bin/env bash

set -x
set -euo pipefail

########################################
# @return string
########################################
function usage() {
    echo "
NAME ${0} -- Run container image
SYNOPSIS
    ${0} APP_VERSION
EXAMPLES
    ${0} 1.0.0
"
}

app_name="$(basename $(git rev-parse --show-toplevel))"
app_version="${1}"
image_name="${app_name}:${app_version}"
port=5000

docker run -d -p ${port}:${port} ${image_name}
