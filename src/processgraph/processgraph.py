from processgraph.node import Node


class ProcessGraph:
    """A graph containing nodes and edges."""

    def __init__(self):

        self._nodes = {}

        self._edges = []

    def add_node(self, node: Node):

        self._nodes[node.label] = node