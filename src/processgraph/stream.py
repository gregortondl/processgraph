from dataclasses import dataclass, field
from typing import Any

from processgraph.analysis import Analysis


@dataclass(slots=True)
class Stream:
    """A process stream."""

    label: str
    source: str
    target: str
    properties: dict[str, Any] = field(default_factory=dict)
    analyses: list[Analysis] = field(default_factory=list)

    def add_analysis(self, analysis: Analysis) -> None:
        """Add an analysis to the stream."""

        self.analyses.append(analysis)

    def remove_analysis(self, analysis: Analysis) -> None:
        """Remove an analysis from the stream."""

        self.analyses.remove(analysis)

    def get_analyses(self) -> list[Analysis]:
        """Return all analyses."""

        return self.analyses