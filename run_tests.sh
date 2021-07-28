#!/usr/bin/env bash

#set -x
# strict mode
set -euo pipefail

wd="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Find virtualenv if applicable
env_activate="${wd}/venv/bin/activate"
if [[ -f "${env_activate}" ]]; then
    set +u
    source "${env_activate}"
    set -u
fi

python -m unittest discover -s ${wd}/tests

if [[ -f "${env_activate}" ]]; then
    set +u
    deactivate
    set -u
fi
