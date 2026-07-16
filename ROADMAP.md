# ProcessGraph Roadmap

ProcessGraph is developed as a layered architecture. Each layer has a well-defined responsibility and builds upon the previous one while maintaining a stable and lightweight graph core.

---

# Version 0.1 – Graph Layer

**Goal:** Build a lightweight, robust, and extensible graph engine.

## Core Classes

- [x] Graph
- [x] Node
- [x] Edge
- [x] Equipment (base class)

## Graph Operations

- [x] Add/remove nodes
- [x] Add/remove edges
- [x] Connect nodes
- [x] Successors
- [x] Predecessors
- [x] Neighbors
- [x] Duplicate edge protection

## Validation

- [x] Self-loop detection

## Serialization

- [x] to_dict()
- [x] from_dict()

## Remaining Tasks

- [ ] Unit tests (pytest)
- [ ] API documentation
- [ ] Performance improvements

---

# Version 0.2 – Process Layer

**Goal:** Introduce process engineering concepts while keeping the graph layer independent.

## Equipment

- [x] Equipment
- [x] Pump
- [ ] Valve
- [ ] HeatExchanger
- [ ] Mixer
- [ ] Splitter
- [ ] Separator
- [ ] Reactor
- [ ] PyrolysisReactor
- [ ] Source
- [ ] Sink

## Streams

- [ ] Stream
- [ ] MaterialStream
- [ ] EnergyStream

## Process Topology

- [ ] Ports
- [ ] Junctions
- [ ] Connections
- [ ] Process templates

---

# Version 0.3 – Knowledge Layer

**Goal:** Attach engineering knowledge to process objects.

## Equipment Resources

- [ ] Resource base class
- [ ] Datasheet
- [ ] Manual
- [ ] CAD model
- [ ] P&ID
- [ ] Images

## Stream Analyses

- [ ] Analysis base class
- [ ] ICP-OES
- [ ] CHNS
- [ ] BET
- [ ] FTIR
- [ ] SEM
- [ ] XRD
- [ ] Experimental datasets

## Knowledge Management

- [ ] Metadata
- [ ] Resource linking
- [ ] Search interface


# Version 0.4 – AI Layer

**Goal:** Enable AI-assisted engineering using the process knowledge graph.

## Retrieval

- [ ] Knowledge retrieval
- [ ] Semantic search
- [ ] Vector embeddings

## Engineering Intelligence

- [ ] Engineering assistant
- [ ] Process analysis
- [ ] Design recommendations
- [ ] Knowledge-based reasoning

## AI Interfaces

- [ ] LLM integration
- [ ] Agent tools
- [ ] API interfaces


# Version 0.5 – Engineering Applications

**Goal:** Build complete engineering workflows on top of the knowledge graph.

## Simulation

- [ ] Thermodynamic models
- [ ] Property packages
- [ ] Species and compositions
- [ ] Reaction models
- [ ] Equation-based simulation

## Analysis

- [ ] Graph algorithms
- [ ] Process optimization
- [ ] Design-space exploration
- [ ] Digital twins

## Visualization

- [ ] Interactive process diagrams
- [ ] NetworkX interoperability
- [ ] Web visualization
- [ ] Reporting

---

# Version 1.0 – Stable Public Release

**Goal:** First stable release of the ProcessGraph platform.

- [ ] Stable public API
- [ ] Comprehensive documentation
- [ ] Complete unit test suite
- [ ] Example projects
- [ ] API reference
- [ ] Developer guide
- [ ] First public release