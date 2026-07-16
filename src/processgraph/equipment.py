from dataclasses import dataclass, field
from processgraph.node import Node
from processgraph.resource import Resource


@dataclass
class Equipment(Node):
    """Base class for all process equipment."""

    resources: list[Resource] = field(default_factory=list)

@dataclass
class Pump(Equipment):
    """A pump."""

    pass


@dataclass
class Reactor(Equipment):
    """A reactor."""

    pass


@dataclass
class Valve(Equipment):
    """A valve."""

    pass


@dataclass
class HeatExchanger(Equipment):
    """A heat exchanger."""

    pass