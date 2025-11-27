# Protonox Patch Notes

This file catalogs the Protonox-specific changes expected in each framework component. Update entries when patches are added or refreshed.

## python-for-android
- Target Android API level 34 / Android 15.
- Enable modern recipes: OpenSSL 3.x, Pillow 10+, Cython 3.x, Pyjnius master.
- Hardened build flags for ARM64 and improved `android.py` bootstrap logging.

## kivy-2.3.1-protonox
- TextInput stability and IME handling improvements.
- Universal emoji rendering across platforms.
- Clock frame pacing fixes for smoother animations.
- Canvas acceleration toggles for low-latency redraws.
- Windowser hooks for native services and permissions.
- Cython 3.x compatibility adjustments.

## pyjnius-protonox
- Android 14–15 compatibility for Java bridge bootstrapping.
- Extended `JavaMethodBinder` for complex signatures.
- Native service bridge utilities and AndroidX permission helpers.

## cython-protonox
- ARM64 optimization flags and reproducible builds for python-for-android.
- Config templates for both 0.29.x LTS and 3.x lines depending on P4A constraints.

## buildozer
- Default Android SDK 34 / NDK r25c configuration.
- Java 17 toolchain compatibility.
- Protonox-friendly presets for python-for-android, Kivy, Pyjnius, and Cython 3.x.

## windowser
- Java templates for permissions, storage, notifications, and background services.
- Python facade for bridging Kivy apps with native Android components.

## kibit3
- Emoji-aware text shaping and bidirectional text scaffolding.
- Shared rendering hooks for Kivy and KivyMD widgets.

## bkibit-2.3.1
- Accelerated render path tuned for Android 15 devices.
- Text rendering pipeline prepared for kibit3 interoperability.

## protonox-devtools
- Hot reload watcher compatible with Kivy apps.
- Remote console and WebSocket debugger for wireless inspection.
- Inspector utilities for runtime widget tree introspection.
- CLI commands to orchestrate builds and diagnostics.
