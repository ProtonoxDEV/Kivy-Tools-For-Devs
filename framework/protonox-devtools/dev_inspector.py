"""Runtime inspector placeholder."""

from typing import Any, Dict


def snapshot_state(namespace: Dict[str, Any]) -> Dict[str, str]:
    return {key: type(value).__name__ for key, value in namespace.items()}
