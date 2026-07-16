from dataclasses import dataclass, field


@dataclass
class Analysis:
    """Base class for scientific analyses."""

    name: str
    properties: dict = field(default_factory=dict)


@dataclass
class ICPOES(Analysis):
    """ICP-OES analysis."""

    pass


@dataclass
class CHNS(Analysis):
    """CHNS analysis."""

    pass