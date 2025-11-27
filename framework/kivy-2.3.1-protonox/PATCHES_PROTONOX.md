Planned Protonox patchset for Kivy (apply after upstream sync)
------------------------------------------------------------

- **Emoji engine integration**: wire `kibit3` emoji renderer into the text/layout pipeline
  with fallbacks for platforms lacking native emoji fonts.
- **Clock stability**: backport scheduling fixes for Android background services and enforce
  monotonic timers when available.
- **TextInput enhancements**: improve cursor visibility, selection handling, and IME commit
  processing for Android 13–15.
- **Canvas acceleration**: integrate `bkibit` acceleration hooks for Android, including
  batching and GPU state hints compatible with API 35.
- **Android 15 compatibility**: verify permission prompts, notification channel defaults,
  and window insets handling on target API 35 builds.

Document applied patch IDs and upstream references in this file once the code is synced.
