from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Resource:
    """Base class for engineering resources."""

    name: str
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class Datasheet(Resource):
    """Equipment datasheet."""

    pass


@dataclass(slots=True)
class Manual(Resource):
    """Equipment manual."""

    pass


@dataclass(slots=True)
class CADModel(Resource):
    """CAD model."""

    pass