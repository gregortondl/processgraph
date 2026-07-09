from __future__ import annotations

from dataclasses import dataclass

from processgraph.node import Node


@dataclass(slots=True)
class Edge:
    """A connection between two nodes."""

    source: Node
    target: Node