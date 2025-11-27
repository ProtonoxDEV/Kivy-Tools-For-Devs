from __future__ import annotations

import json
from typing import Any


def serialize_widget(widget: Any) -> dict[str, Any]:
    return {
        "class": widget.__class__.__name__,
        "id": getattr(widget, "id", None),
        "text": getattr(widget, "text", None),
        "children": [serialize_widget(child) for child in getattr(widget, "children", [])],
    }


def export_tree(root_widget: Any, *, pretty: bool = True) -> str:
    payload = serialize_widget(root_widget)
    return json.dumps(payload, indent=2 if pretty else None)
