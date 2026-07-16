from dataclasses import dataclass, field


@dataclass
class Analysis:
    """Base class for scientific analyses."""

    name: str
    properties: dict = field(default_factory=dict)