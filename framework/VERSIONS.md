# Protonox Framework Versions

This document tracks the upstream source and snapshot guidance used to populate the Protonox framework components. Update the values after syncing the latest sources with `tools/update_framework.sh`.

| Component | Upstream | Branch/Tag | Notes |
| --- | --- | --- | --- |
| python-for-android | https://github.com/kivy/python-for-android | master | Target Android 15 SDK/NDK and modern recipes (openssl/pillow/cython/pyjnius). |
| kivy-2.3.1-protonox | https://github.com/kivy/kivy | master | Protonox patches applied on top of latest Kivy to replace legacy 2.3.1 label. |
| pyjnius-protonox | https://github.com/kivy/pyjnius | master | Android 14–15 compatibility and Protonox bridge additions. |
| cython-protonox | https://github.com/cython/cython | latest stable 3.x (or 0.29.x if required) | Optimized for ARM64 compilation with python-for-android. |
| buildozer | https://github.com/kivy/buildozer | master | Adjusted for Android SDK 34, NDK r25c, Java 17. |
| windowser | Protonox native layer | protonox-head | Java + Python bridges for permissions, storage, notifications, background services. |
| kibit3 | Protonox text engine | protonox-head | Emoji-capable text shaping for Kivy/KivyMD. |
| bkibit-2.3.1 | Protonox render engine | protonox-head | Lightweight accelerated renderer targeting Android 15. |
| protonox-devtools | Protonox tools | protonox-head | Hot reload, remote console, inspector, CLI. |
