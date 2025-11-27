# Protonox DevTools

Developer utilities for Protonox apps, including hot reload, remote debugging, inspector, and CLI orchestration.

## Modules
- `hot_reload.py`: Watches source files and triggers app reload callbacks.
- `watcher.py`: File system watcher built on `watchdog`-style polling (no external deps).
- `remote_console.py`: Simple TCP console for issuing runtime commands.
- `ws_debugger.py`: WebSocket-style debug stub (falls back to TCP if websockets unavailable).
- `devtools_inspector.py`: Runtime widget inspector helpers.
- `protonox`: CLI entry point supporting doctor/create/build commands.

These modules avoid heavyweight dependencies and are intended as scaffolding that can be expanded in downstream projects.
