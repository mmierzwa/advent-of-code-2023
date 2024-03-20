#!/usr/bin/env bash
set -e

./"$(dirname "$0")"/../.venv/bin/python "$(dirname "$0")"/../src/tasks/"$1"/main.py "$(dirname "$0")"/../src/tasks/"$1"/"$2"