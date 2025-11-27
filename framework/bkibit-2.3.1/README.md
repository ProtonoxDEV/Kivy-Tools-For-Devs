# BKibit 2.3.1 (Protonox Renderer)

BKibit provides a lightweight render pipeline intended to pair with Kibit3 text shaping. The implementation here is a minimal scaffold ready for acceleration.

## Features
- Batched instruction queue for text rendering.
- Hooks to integrate GPU acceleration or custom canvas backends.
- Designed for Android 15 optimizations.

## Quickstart
```python
from bkibit.renderer import Renderer
r = Renderer()
r.enqueue({"text": "Hello", "emoji": False, "order": 0})
r.render()
```
