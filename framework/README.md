# Protonox Framework Components

This folder hosts Protonox-maintained forks and toolchain components. Because this repository does not vendor upstream git history, each component should be populated by cloning the specified upstream repository, removing its `.git` folder, and applying Protonox patches described in `PATCHES.md`.

> NOTE: Network access may be restricted in CI environments. If cloning fails, populate the folders manually using pre-fetched archives.

## Layout
- `python-for-android`: Patched for Android 15+, bundled recipes (OpenSSL, Pillow, Cython, Pyjnius).
- `kivy-2.3.1-protonox`: Latest Kivy with Protonox emoji/TextInput/Clock/canvas patches.
- `pyjnius-protonox`: Pyjnius with Android 15 compatibility and Firebase SDK interoperability.
- `cython-protonox`: Optimized Cython distribution targeting ARM64.
- `buildozer`: Internal Buildozer snapshot preconfigured for Protonox workflows.
- `windowser`: Native layer for storage, permissions, notifications, and background services.
- `kibit3` & `bkibit-2.3.1`: Text and emoji rendering engines for cross-platform use.
- `protonox-devtools`: Hot reload, wireless debugging, remote console, inspector, and CLI.

See `VERSIONS.md` for upstream references and `PATCHES.md` for Protonox customizations.
