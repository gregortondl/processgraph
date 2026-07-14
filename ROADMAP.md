# ProcessGraph Roadmap

The development of ProcessGraph follows a layered architecture. Each version extends the capabilities of the previous one while keeping the graph core stable and independent.

---

# Version 0.1 – Graph Core

Goal: Build a lightweight, robust, and extensible graph engine.

## Core Classes

- [x] Node
- [x] Edge
- [x] Graph
- [x] Equipment (base class)

## Graph Operations

- [x] Add nodes
- [x] Add edges
- [x] Connect nodes
- [x] Successors
- [x] Predecessors
- [x] Neighbors
- [x] Duplicate edge protection

## Remaining Tasks

- [ ] Graph validation
- [ ] Serialization
- [ ] Unit tests
- [ ] Documentation

---

# Version 0.2 – Process Engineering

Goal: Introduce process engineering concepts without changing the graph core.

## Components

- [ ] Ports
- [ ] Material streams
- [ ] Process equipment
- [ ] Sources
- [ ] Sinks
- [ ] Junctions

## Equipment Library

- [ ] Pump
- [ ] Valve
- [ ] Heat Exchanger
- [ ] Mixer
- [ ] Splitter
- [ ] Reactor
- [ ] Pyrolysis Reactor

---

# Version 0.3 – Scientific Modeling

Goal: Support scientific process modeling.

- [ ] Property system
- [ ] Thermodynamic properties
- [ ] Species and compositions
- [ ] Reaction models
- [ ] Equation system

---

# Version 0.4 – Analysis & Visualization

Goal: Analyze and visualize process graphs.

- [ ] JSON serialization
- [ ] NetworkX interoperability
- [ ] Graph algorithms
- [ ] Visualization
- [ ] Interactive process diagrams

---

# Version 0.5 – AI & Optimization

Goal: Build an AI-ready process engineering platform.

- [ ] Optimization
- [ ] Design-space exploration
- [ ] AI interfaces
- [ ] LLM integration
- [ ] Automated model generation
- [ ] Engineering assistants

---

# Version 1.0 – Stable Public API

Goal: First stable release.

- [ ] Stable public API
- [ ] Comprehensive documentation
- [ ] Complete unit test suite
- [ ] Example projects
- [ ] API reference
- [ ] First official release