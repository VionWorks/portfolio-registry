# VionWorks Portfolio Registry

Canonical registry and governance system for Alexi Vion's public professional projects.

VionWorks separates projects by the kind of professional evidence they provide, while keeping one structured inventory that can scale from a handful of repositories to thousands.

## Project families

| Prefix | Type | Purpose |
|---|---|---|
| `TECH` | Technical Lab | Demonstrate specific engineering capability |
| `DEMO` | Business Demo | Demonstrate delivery against a concrete business problem |
| `PROD` | Product | Track real software/products intended for actual use |
| `RES` | Research | Track research, reproductions, benchmarks, and studies |
| `PLAY` | Playground | Track lightweight experiments that do not yet justify a larger project |

See [`taxonomy/TYPES.md`](taxonomy/TYPES.md) for the canonical definitions.

## Registered projects

| ID | Project | Type | Domain | Status | Featured |
|---|---|---|---|---|---:|
| [`TECH-001`](projects/TECH-001.yaml) | [RAG Architecture Lab](https://github.com/AlexiVion/rag-architecture-lab) | Technical Lab | Artificial Intelligence | Published | Yes |
| [`DEMO-001`](projects/DEMO-001.yaml) | [Casa Luma](https://github.com/AlexiVion/hospitality-casa-luma) | Business Demo | Hospitality | Building | No |
| [`DEMO-002`](projects/DEMO-002.yaml) | [Brisas de la Cayana](https://github.com/VionWorks/hospitality-brisas-de-la-cayana) | Business Demo | Hospitality | Planning | No |

Project entries in [`projects/`](projects/) are the canonical source of truth.

## Lifecycle

```text
idea -> planning -> building -> qa -> published
                    |               |
                    +-------------> archived

published -> building
published -> archived
```

See [`taxonomy/STATUS.md`](taxonomy/STATUS.md).

## Repository naming

Project IDs are permanent registry identifiers and are **not** embedded in repository names.

Good examples:

```text
rag-architecture-lab
agent-architecture-lab
hospitality-casa-luma
dental-nova
```

See [`taxonomy/NAMING.md`](taxonomy/NAMING.md).

## Structure

```text
portfolio-registry/
├── README.md
├── SCHEMA.md
├── projects/
│   ├── TECH-001.yaml
│   ├── DEMO-001.yaml
│   └── DEMO-002.yaml
├── taxonomy/
│   ├── TYPES.md
│   ├── STATUS.md
│   ├── NAMING.md
│   └── DOMAINS.md
├── scripts/
│   └── validate_registry.py
└── .github/
    └── workflows/
        └── validate-registry.yml
```

## Source-of-truth rules

1. Every registered project has exactly one file in `projects/`.
2. Project IDs are permanent and never reused.
3. Registering a project does not require moving its repository into the VionWorks organization.
4. Repository presentation and technical documentation remain inside each project repository.
5. The registry contains classification and portfolio metadata only—never secrets, credentials, client data, or sensitive configuration.
6. `featured: true` means a project is eligible for curated public surfaces; it does not mean every featured project must always be pinned.

The complete metadata contract is defined in [`SCHEMA.md`](SCHEMA.md).

## Validation

Run locally:

```bash
python -m pip install pyyaml
python scripts/validate_registry.py
```

A lightweight GitHub Actions workflow validates metadata changes. It does not run project benchmarks, model workloads, or application test suites.

## Adding a project

1. Decide the project's primary family (`TECH`, `DEMO`, `PROD`, `RES`, or `PLAY`).
2. Allocate the next permanent ID in that family.
3. Create `projects/<ID>.yaml` using the schema.
4. Validate the registry.
5. Add `PROJECT.yaml` to the project repository when appropriate so the repository can carry a local copy of its public classification metadata.
6. Update curated public surfaces only if the project is ready to represent VionWorks professionally.

## First registered projects

`TECH-001` is **RAG Architecture Lab**, a public technical lab focused on implementing, benchmarking, and comparing Retrieval-Augmented Generation architectures under controlled conditions.

`DEMO-001` is **Casa Luma**, a fictional boutique-hotel concept project focused on direct booking, room discovery, and conversion-oriented hospitality UX. It is explicitly a concept project rather than client work.

`DEMO-002` is **Brisas de la Cayana**, a prospect demo for a real accommodation in Villa Alpina. It focuses on hospitality storytelling, direct-contact conversion, and turning existing property photography and business information into a stronger owned web experience. Until it becomes client work, it must be presented as a prospect demo rather than a paid client project.
