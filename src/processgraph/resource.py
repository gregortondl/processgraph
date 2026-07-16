from dataclasses import dataclass, field


@dataclass
class Resource:
    """Base class for engineering resources."""

    name: str
    properties: dict = field(default_factory=dict)


@dataclass
class Datasheet(Resource):
    """Equipment datasheet."""

    pass


@dataclass
class Manual(Resource):
    """Equipment manual."""

    pass


@dataclass
class CADModel(Resource):
    """CAD model."""

    pass