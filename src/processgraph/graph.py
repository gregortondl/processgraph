



from processgraph.node import Node
from processgraph.edge import Edge
from processgraph.stream import Stream
from processgraph.equipment import Equipment


class Graph:
    """A graph of nodes connected by edges."""

    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []

        self.equipment: dict[str, Equipment] = {}
        self.streams: dict[str, Stream] = {}

    def add_node(self, node: Node) -> None:
        """Add a node to the graph."""

        if node.label in self.nodes:
            raise ValueError(f"Node '{node.label}' already exists.")

        self.nodes[node.label] = node

    def add_equipment(self, equipment: Equipment) -> None:
        """Add equipment to the graph."""

        self.add_node(equipment)
        self.equipment[equipment.label] = equipment

    def add_stream(self, stream: Stream) -> None:
        """Add a stream to the graph."""

        self.streams[stream.label] = stream

        self.connect(
        stream.source,
        stream.target,
             )
        
    def get_stream(self, label: str) -> Stream:
         """Return a stream by label."""

         return self.streams[label] 

    def find_stream(self, label: str) -> Stream | None:
         """Return a stream by label or None if it does not exist."""

         return self.streams.get(label)
    
    def contains_stream(self, label: str) -> bool:
         """Return True if a stream with the given label exists."""

         return label in self.streams

    def remove_node(self, node: Node) -> None:
        """Remove a node from the graph."""

        for edge in self.edges.copy():
            if edge.source == node or edge.target == node:
                self.remove_edge(edge)


        del self.nodes[node.label]

    def get_node(self, label: str) -> Node:
        """Return a node by label."""

        return self.nodes[label]
    
        
    
    def find_node(self, label: str) -> Node | None:
        """Return a node by label or None if it does not exist."""

        return self.nodes.get(label)
    
    def contains_node(self, label: str) -> bool:
        """Return True if a node with the given label exists."""

        return label in self.nodes

    def add_edge(self, edge: Edge) -> None:
        """Add an edge to the graph."""

        if edge.source.label not in self.nodes:
            raise ValueError(f"Unknown source node '{edge.source.label}'.")

        if edge.target.label not in self.nodes:
            raise ValueError(f"Unknown target node '{edge.target.label}'.")
       
        if self.has_edge(edge.source, edge.target):
            raise ValueError(f"Edge '{edge.source.label} -> {edge.target.label}' already exists.")

        self.edges.append(edge)

    def remove_edge(self, edge: Edge) -> None:
        """Remove an edge from the graph."""

        self.edges.remove(edge)  
    
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

    def validate(self) -> list[str]:
        """Validate the graph."""

        errors = []

        for edge in self.edges:
            if edge.source == edge.target:
                errors.append(f"Self-loop: '{edge.source.label}'.")

        return errors
    
    def to_dict(self) -> dict:
        """Return the graph as a dictionary."""

        return {
            "nodes": [
                {
                    "label": node.label,
                    "properties": node.properties,
                }
                for node in self.nodes.values()
            ],
            "edges": [
                {
                    "source": edge.source.label,
                    "target": edge.target.label,
                }
                for edge in self.edges
            ],
        
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Graph":
        """Create a graph from a dictionary."""

        graph = cls()


        for node_data in data["nodes"]:
            node = Node(
                label=node_data["label"],
                properties=node_data["properties"],
            )

            graph.add_node(node)
        for edge_data in data["edges"]:
            source = graph.get_node(edge_data["source"])
            target = graph.get_node(edge_data["target"])

           
            graph.connect(source, target)

        return graph


    def connect(self, source: Node, target: Node) -> None:
        """Connect two nodes."""

        edge = Edge(
            source=source,
            target=target,
        )

        self.add_edge(edge)

    

    def disconnect(self, source: Node, target: Node) -> None:
        """Disconnect two nodes."""

        for edge in self.edges.copy():
            if edge.source == source and edge.target == target:
                self.remove_edge(edge)
                return

        raise ValueError(
            f"Edge '{source.label} -> {target.label}' does not exist."
        )