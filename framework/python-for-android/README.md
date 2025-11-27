Protonox python-for-android fork
================================

This folder is reserved for the upstream `python-for-android` sources patched for Protonox.
Because this workspace does not have internet access, the upstream code must be synchronized
by running the sync script once connectivity is available.

Expected setup steps (documented for future maintainers):

1. Clone upstream with a shallow checkout of `master`.
2. Record the upstream commit in `VERSION.txt`.
3. Apply Protonox patches for Android 15, NDK r25c, and Python 3.11 toolchains.
4. Run the compatibility smoke tests for recipe changes and target API 35 builds.

Until upstream code is synced, this file documents the intent and constraints for the fork.
