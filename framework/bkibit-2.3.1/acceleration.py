"""Acceleration settings for GPU-backed rendering."""

from dataclasses import dataclass


@dataclass
class AccelerationProfile:
    batching_enabled: bool = True
    hint_vulkan: bool = True
    api_level: int = 35


def default_profile() -> AccelerationProfile:
    return AccelerationProfile()
