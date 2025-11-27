# Windowser (Protonox Native Layer)

Windowser provides Protonox-native integrations for Android permissions, storage, notifications, and background services. Java templates are included for integration with python-for-android builds; Python facades route Kivy app requests to the native side.

## Contents
- `android/src/com/protonox/*.java`: Java templates for activities, services, permissions, and storage bridges.
- `python/`: Python side helpers for registering services and dispatching commands.

## Usage
1. Copy the Java sources into your Android project (e.g., `src/main/java/com/protonox`).
2. Include the Python helpers in your app and wire them to Pyjnius bridges.
3. Grant required permissions in `AndroidManifest.xml` (storage, notifications, foreground services as needed).

## Notes
These templates are lightweight and should be expanded with project-specific logic. See `../PATCHES.md` for expected Protonox behaviors.
