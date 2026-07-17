from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Analysis:
    """Base class for scientific analyses."""

    name: str
    properties: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ICPOES(Analysis):
    """ICP-OES analysis."""

    pass


@dataclass(slots=True)
class CHNS(Analysis):
    """CHNS analysis."""

    pass