# Buildozer (Protonox Configuration)

Expected source: https://github.com/kivy/buildozer (branch: master)

## Protonox Adjustments
- Default Android SDK 34 / NDK r25c values.
- Compatibility with Java 17 toolchains.
- Presets for python-for-android + Kivy + Pyjnius + Cython 3.x stacks.

## Sync Checklist
1. `git clone --depth=1 https://github.com/kivy/buildozer .`
2. Remove `.git` directory.
3. Apply Protonox configuration diffs; capture details in `../PATCHES.md`.
4. Record upstream commit hash in `../VERSIONS.md`.
