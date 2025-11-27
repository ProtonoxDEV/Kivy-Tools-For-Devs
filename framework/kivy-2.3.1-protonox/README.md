Protonox Kivy fork
==================

This directory will hold the upstream Kivy sources with Protonox patches applied. Network
access is unavailable in this workspace, so the upstream repository is not cloned yet.

Planned Protonox patches (to apply after syncing upstream):
- Integrate the `kibit3` emoji/text pipeline.
- Stabilize `Clock` scheduling for background services.
- Improve `TextInput` IME handling and selection behavior.
- Accelerate canvas rendering with the `bkibit` pipeline and Android 15 GPU hints.
- Validate Android 15 compatibility for input, notifications, and permissions glue.

See `PATCHES_PROTONOX.md` for the detailed patch checklist.
