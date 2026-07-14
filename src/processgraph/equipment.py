from dataclasses import dataclass, field

from processgraph.node import Node


@dataclass
class Equipment(Node):
    """Base class for all process equipment."""

    resources: list = field(default_factory=list)

