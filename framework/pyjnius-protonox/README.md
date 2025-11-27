# Pyjnius (Protonox Bridge)

Expected source: https://github.com/kivy/pyjnius (branch: master)

## Protonox Enhancements
- Android 14–15 bootstrap compatibility.
- Extended `JavaMethodBinder` for complex signatures.
- Native service bridge helpers and AndroidX permission wrappers.

## Sync Checklist
1. `git clone --depth=1 https://github.com/kivy/pyjnius .`
2. `rm -rf .git`
3. Apply Protonox patches per `../PATCHES.md`.
4. Document the upstream commit hash in `../VERSIONS.md`.
