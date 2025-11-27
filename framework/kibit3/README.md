# Kibit3 (Protonox Text Engine)

Kibit3 provides emoji-aware text shaping scaffolding for Protonox apps. It is designed to integrate with both Kivy and KivyMD widgets while remaining lightweight.

## Features
- Unicode emoji fallback table to keep rendering consistent across platforms.
- Simple text shaping hooks to plug into Kivy canvas operations.
- Minimal dependencies to remain python-for-android friendly.

## Quickstart
```python
from kibit3.engine import TextEngine
engine = TextEngine()
segments = engine.shape("Hello 🌎")
```
