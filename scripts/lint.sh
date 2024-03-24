#!/usr/bin/env bash
set -e

./"$(dirname "$0")"/../.venv/bin/mypy "$(dirname "$0")"/../src/tasks/"$1"/