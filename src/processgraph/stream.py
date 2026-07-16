from dataclasses import dataclass, field

from processgraph.equipment import Equipment
from processgraph.analysis import Analysis

@dataclass
class Stream:
    """Base class for all process streams."""

    label: str

    source: Equipment
    target: Equipment

    properties: dict = field(default_factory=dict)
    analyses: list[Analysis] = field(default_factory=list)