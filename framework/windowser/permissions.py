"""
Runtime permission helpers for Protonox applications.
This module is designed to be called from Kivy/Pyjnius code.
"""

from dataclasses import dataclass
from typing import Iterable, List

@dataclass
class PermissionRequest:
    permissions: List[str]
    request_code: int = 1001


def pending_permissions(granted: Iterable[str], required: Iterable[str]) -> List[str]:
    granted_set = set(granted)
    return [perm for perm in required if perm not in granted_set]


def format_android_permissions(permissions: Iterable[str]) -> List[str]:
    return [perm.strip() for perm in permissions if perm.strip()]
