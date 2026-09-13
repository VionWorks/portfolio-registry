# Project types

VionWorks uses five top-level project families. Every registered project belongs to exactly one.

## TECH — Technical Labs

**Metadata value:** `technical-lab`

Purpose: demonstrate specific engineering capability through inspectable implementation, measurement, architecture decisions, tests, or reproducible experiments.

Typical examples:

- RAG architecture benchmarking
- agent architecture evaluation
- vector search experiments
- LLM routing systems
- observability architecture labs

A TECH project is primarily evidence of **technical competence**.

## DEMO — Commercial / Business Demos

**Metadata value:** `business-demo`

Purpose: demonstrate the ability to solve a concrete business problem through a polished concept project or sales demo.

Typical examples:

- hospitality direct-booking website
- dental lead-generation website
- restaurant ordering experience
- real-estate property discovery flow

A DEMO project is primarily evidence of **business problem solving and delivery**.

## PROD — Real Products

**Metadata value:** `product`

Purpose: software or systems intended for real users, customers, operations, or commercial use.

Typical examples:

- SaaS products
- production services
- operational platforms
- shipped internal products when appropriate to register

A PROD project is a **real product**, not a portfolio simulation.

## RES — Research

**Metadata value:** `research`

Purpose: investigate a research question, reproduce published work, compare methods, or produce a research artifact where the research contribution is the main point.

Typical examples:

- paper reproductions
- benchmark studies
- ablation studies not attached to a broader technical lab
- research notes with code and results

A RES project is primarily evidence of **research methodology and reasoning**.

## PLAY — Experiments / Playground

**Metadata value:** `playground`

Purpose: lightweight exploration that does not yet justify a standalone professional project.

Typical examples:

- UI experiments
- API trials
- component prototypes
- short agent experiments
- throwaway technical spikes

Small PLAY work should usually live in a shared playground repository rather than creating a new repository for every experiment.

## Classification rule

Classify by the project's **primary reason for existing**, not by its technology.

For example, a hotel website written in Next.js remains `DEMO`, while a Next.js rendering benchmark designed to study framework behavior may be `TECH` or `RES`.
