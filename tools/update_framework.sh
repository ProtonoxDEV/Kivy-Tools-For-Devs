#!/usr/bin/env bash
set -euo pipefail

# This script documents how to sync Protonox dependencies from upstream sources.
# It intentionally uses shallow clones and removes .git metadata to keep the
# repository lightweight. Run from the repository root.

ROOT_DIR=$(cd "$(dirname "$0")/.." && pwd)
FRAMEWORK_DIR="$ROOT_DIR/framework"

sync_component() {
  local name=$1
  local repo=$2
  local branch=${3:-master}
  local target="$FRAMEWORK_DIR/$name"

  echo "[Protonox] Syncing $name from $repo ($branch)"
  rm -rf "$target"/.git
  git clone --depth=1 --branch "$branch" "$repo" "$target" || {
    echo "Warning: clone failed for $name; ensure sources are provided manually." >&2
    return 0
  }
  rm -rf "$target/.git"
}

# Upstream components
sync_component "python-for-android" "https://github.com/kivy/python-for-android" "master"
sync_component "kivy-2.3.1-protonox" "https://github.com/kivy/kivy" "master"
sync_component "pyjnius-protonox" "https://github.com/kivy/pyjnius" "master"
sync_component "cython-protonox" "https://github.com/cython/cython" "master"
sync_component "buildozer" "https://github.com/kivy/buildozer" "master"

cat <<INFO
Manual components (populate manually if clones are not available):
- windowser
- kibit3
- bkibit-2.3.1
- protonox-devtools
INFO
