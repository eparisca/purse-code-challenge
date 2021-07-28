#!/usr/bin/env bash

set -x
set -euo pipefail

########################################
# @return string
########################################
function usage() {
  echo "
NAME ${0} -- Push a container image into a Kubernetes cluster's default namespace
SYNOPSIS
    ${0} APP_VERSION
EXAMPLES
    ${0} 1.0.0
"
}

wd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

export app_name="$(basename $(git rev-parse --show-toplevel))"
export namespace="default"
export port_num="80"
export image_version="1.0.0"
export min_replicas=3
export max_replicas=9

input_file="${wd}/kubernetes/manifest-template.yaml"
manifest="${wd}/manifest.yaml"

envsubst < ${input_file} > ${manifest}

#kubectl apply -f ${manifest}