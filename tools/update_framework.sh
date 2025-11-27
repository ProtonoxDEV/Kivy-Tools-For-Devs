#!/usr/bin/env bash
set -euo pipefail

echo "Syncing Protonox framework components via sync_framework.py"
python3 "$(dirname "$0")/sync_framework.py"
