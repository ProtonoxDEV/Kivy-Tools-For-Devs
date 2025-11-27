# Kivy (Protonox Build)

Expected source: https://github.com/kivy/kivy (branch: master)

## Protonox Patches
See `../PATCHES.md` for the full list. Key items include TextInput stability, emoji rendering, Clock pacing fixes, canvas acceleration hooks, and windowser integration.

## Sync Checklist
1. `git clone --depth=1 https://github.com/kivy/kivy .`
2. `rm -rf .git`
3. Apply Protonox patches and document them in `PATCHES_PROTONOX.md` in this folder.
4. Update `../VERSIONS.md` with the commit hash used.
