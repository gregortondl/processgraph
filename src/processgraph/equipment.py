from dataclasses import dataclass, field


@dataclass
class Equipment:
   
    """
    Base class for all process equipment.

    Equipment is connected to the process graph through nodes.
    """
    label: str
    properties: dict = field(default_factory=dict)