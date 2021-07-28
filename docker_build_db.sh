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

app_name="purse-db"
app_version="${1}"
image_name="${app_name}:${app_version}"
port=5432

docker build db -f Dockerfile.postgres \
    --label maintainer="Emilio Parisca <eparisca@gmail.com>" \
    --label org.label-schema.build-date=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
    --label org.label-schema.version="${app_version}" \
    -t "${image_name}"

docker run -d \
  --name ${app_name} \
  -p ${port}:${port} \
  ${image_name}