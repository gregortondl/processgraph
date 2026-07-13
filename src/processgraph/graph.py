from processgraph.node import Node
from processgraph.edge import Edge


class Graph:
    """A graph of nodes connected by edges."""

    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []

    def add_node(self, node: Node) -> None:
        """Add a node to the graph."""

        if node.label in self.nodes:
            raise ValueError(f"Node '{node.label}' already exists.")

        self.nodes[node.label] = node

    def get_node(self, label: str) -> Node:
        """Return a node by label."""

        return self.nodes[label]

    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the graph."""

        if edge.source.label not in self.nodes:
            raise ValueError(f"Unknown source node '{edge.source.label}'.")

        if edge.target.label not in self.nodes:
            raise ValueError(f"Unknown target node '{edge.target.label}'.")
       
        if self.has_edge(edge.source, edge.target):
            raise ValueError(f"Edge '{edge.source.label} -> {edge.target.label}' already exists.")

        self.edges.append(edge)
        
    
    def has_edge(self, source: Node, target: Node) -> bool:
        """Return True if an edge exists."""

        for edge in self.edges:
            if edge.source == source and edge.target == target:
                return True

        return False

    def successors(self, node: Node) -> list[Node]:
        """Return all direct successor nodes."""

        successors = []

        for edge in self.edges:
            if edge.source == node:
                successors.append(edge.target)

        return successors
    
    def predecessors(self, node: Node) -> list[Node]:
        """Return all direct predecessor nodes."""

        predecessors = []

        for edge in self.edges:
            if edge.target == node:
                predecessors.append(edge.source)

        return predecessors

            
    def neighbors(self, node: Node) -> list[Node]:
        """Return all neighboring nodes."""

        neighbors = []

        for edge in self.edges:
            if edge.source == node:
                neighbors.append(edge.target)

            elif edge.target == node:
                neighbors.append(edge.source)

        return neighbors

    def connect(self, source: Node, target: Node) -> None:
        """Connect two nodes."""

        edge = Edge(
            source=source,
            target=target,
        )

        self.add_edge(edge)