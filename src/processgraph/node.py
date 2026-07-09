from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Node:
    """A node in a ProcessGraph."""

    label: str
    properties: dict[str, Any] = field(default_factory=dict)