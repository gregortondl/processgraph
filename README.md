# ProcessGraph

**ProcessGraph** is an open-source Python framework for graph-based modeling of industrial process systems.

The project provides a lightweight and extensible graph engine as the foundation for process engineering, scientific computing, optimization, and AI-assisted engineering applications.

---

## Vision

ProcessGraph separates the **graph engine** from the **process engineering domain**.

```
                ProcessGraph Core
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
 Process Engineering  Energy Systems  AI Applications
```

The graph core remains independent of thermodynamics, process simulation, and optimization. Domain-specific functionality is built on top of the graph rather than being embedded into it.

This architecture enables ProcessGraph to evolve into a flexible research platform for:

- Industrial process modeling
- Process simulation
- Digital twins
- Equation-based modeling
- Optimization
- AI-assisted engineering
- Reinforcement learning environments

---

## Core Architecture

The current architecture is intentionally simple.

```
Graph
│
├── Node
├── Edge
└── Equipment
```

Future extensions will introduce additional layers while keeping the graph core independent.

```
Graph
│
├── Node
├── Edge
└── Equipment
      │
      └── Stream
            │
            ├── Thermodynamics
            ├── Reaction Models
            └── Process Simulation
```

---

## Current Features

The current implementation already provides:

- Graph
- Node
- Edge
- Equipment (base class)
- Graph traversal
    - successors()
    - predecessors()
    - neighbors()
- Edge validation
- Duplicate edge protection

---

## Example

```python
from processgraph.graph import Graph
from processgraph.node import Node

graph = Graph()

pump = Node(label="Pump")
reactor = Node(label="Reactor")

graph.add_node(pump)
graph.add_node(reactor)

graph.connect(pump, reactor)

print(graph.successors(pump))
```

---

## Design Principles

ProcessGraph is built around a few simple principles:

- Graph-first architecture
- Small and extensible core
- Clear separation of graph, engineering, and simulation
- Modern Python development practices
- AI-ready architecture
- Open-source and research-oriented

---

## Long-Term Goals

Future development will include:

- Process equipment library
- Material stream models
- Thermodynamic property packages
- Equation-based simulation
- Optimization algorithms
- Interactive visualization
- NetworkX interoperability
- AI integration through modern LLM APIs

---

## Project Structure

```
processgraph/
│
├── src/
│   └── processgraph/
│       ├── graph.py
│       ├── node.py
│       ├── edge.py
│       └── equipment.py
│
├── sandbox/
├── README.md
├── ROADMAP.md
├── pyproject.toml
└── uv.lock
```

---

## Development Status

ProcessGraph is currently under active development.

The focus of the current development phase is the implementation of a robust and well-tested graph core before expanding into process engineering functionality.

---

## Roadmap

See **ROADMAP.md** for the planned development roadmap.

---

## License

An open-source license (MIT or BSD) will be added before the first stable release.