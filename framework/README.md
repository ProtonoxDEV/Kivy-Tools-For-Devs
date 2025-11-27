# Protonox Framework Components

This folder hosts Protonox-maintained forks and toolchain components. Upstream sources must be
synced when network access is available; the current workspace provides scaffolding, Protonox
probes, and integration hooks so patches can be applied quickly once the real code is fetched.

Included components:
- `python-for-android`: planned patches for Android 15/API 35, NDK r25c, and Python 3.11 toolchain.
- `kivy-2.3.1-protonox`: upstream Kivy with Protonox emoji, text input, clock, and canvas updates.
- `pyjnius-protonox`: AndroidX-aware bridge with extended permissions and service bindings.
- `cython-protonox`: Cython distribution tuned for ARM64 builds inside python-for-android.
- `windowser`: native glue layer for permissions, storage, notifications, and background services.
- `kibit3` & `bkibit-2.3.1`: text/emoji pipeline and canvas acceleration hooks for Protonox Kivy.
- `buildozer`: Protonox defaults for SDK 34, NDK r25c, Java 17, and p4a integration.
- `protonox-devtools`: hot reload, remote console, template generator, and diagnostics.

Refer to `VERSIONS.md` for sync status and to `PATCHES.md` for Protonox-specific patch notes.
