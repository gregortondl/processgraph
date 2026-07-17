from dataclasses import dataclass, field

from processgraph.node import Node
from processgraph.resource import Resource


@dataclass
class Equipment(Node):
    """Base class for all process equipment."""

    resources: list[Resource] = field(default_factory=list)

    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the equipment."""

        self.resources.append(resource)

    def remove_resource(self, resource: Resource) -> None:
        """Remove a resource from the equipment."""

        self.resources.remove(resource)

    def get_resources(self) -> list[Resource]:
        """Return all resources."""

        return self.resources


@dataclass(slots=True)
class Pump(Equipment):
    """A pump."""

    pass


@dataclass(slots=True)
class Reactor(Equipment):
    """A reactor."""

    pass


@dataclass(slots=True)
class Valve(Equipment):
    """A valve."""

    pass


@dataclass(slots=True)
class HeatExchanger(Equipment):
    """A heat exchanger."""

    pass