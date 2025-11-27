# python-for-android (Protonox Snapshot)

Expected source: https://github.com/kivy/python-for-android (branch: master)

## Protonox Notes
- Prepare builds for Android API 34 / Android 15.
- Ensure modern recipes are enabled: `openssl`, `pillow`, `cython`, `pyjnius`.
- Remove upstream `.git` directory after syncing to keep this repository clean.

## Sync Checklist
1. `git clone --depth=1 https://github.com/kivy/python-for-android .` inside this folder.
2. `rm -rf .git` to strip history.
3. Apply Protonox patches documented in `../PATCHES.md`.
4. Record the upstream commit hash in `../VERSIONS.md`.
