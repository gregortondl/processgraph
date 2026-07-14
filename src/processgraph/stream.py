from dataclasses import dataclass, field

from processgraph.equipment import Equipment


@dataclass
class Stream:
    """Base class for all process streams."""

    label: str

    source: Equipment
    target: Equipment

    properties: dict = field(default_factory=dict)
    resources: list = field(default_factory=list)