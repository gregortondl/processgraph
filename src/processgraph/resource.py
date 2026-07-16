from dataclasses import dataclass, field


@dataclass
class Resource:
    """Base class for engineering resources."""

    name: str
    properties: dict = field(default_factory=dict)