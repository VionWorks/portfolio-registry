# Project metadata schema

Every project tracked by VionWorks is represented by exactly one canonical file in `projects/`.

The project file is the source of truth for classification and portfolio metadata. Repository READMEs may repeat selected fields for presentation, but they must not redefine the registry taxonomy.

## Required fields

```yaml
schema_version: 1
id: TECH-001
name: RAG Architecture Lab
slug: rag-architecture-lab
type: technical-lab
domain: artificial-intelligence
areas:
  - rag
  - information-retrieval
status: published
visibility: public
purpose:
  - technical-portfolio
stack:
  - python
featured: true
repository: https://github.com/AlexiVion/rag-architecture-lab
live_demo: null
```

### `schema_version`

Integer identifying the metadata schema. Current value: `1`.

### `id`

Permanent VionWorks project identifier.

Format:

```text
<FAMILY>-<NUMBER>
```

Allowed families:

- `TECH` — Technical Labs
- `DEMO` — Commercial / Business Demos
- `PROD` — Real Products
- `RES` — Research
- `PLAY` — Experiments / Playground

The numeric part uses at least three digits. Existing IDs are never recycled.

Examples: `TECH-001`, `DEMO-014`, `RES-1024`.

### `name`

Human-readable project name.

### `slug`

Stable lowercase kebab-case identifier. It normally matches the repository name but does not have to if a repository is later moved.

### `type`

One of:

- `technical-lab`
- `business-demo`
- `product`
- `research`
- `playground`

See `taxonomy/TYPES.md`.

### `domain`

Primary subject or business domain. Domains are intentionally broader than `areas`.

See `taxonomy/DOMAINS.md`.

### `areas`

One or more focused technical or business areas. Examples: `rag`, `evaluation`, `hospitality`, `direct-booking`.

### `status`

One of:

- `idea`
- `planning`
- `building`
- `qa`
- `published`
- `archived`

See `taxonomy/STATUS.md`.

### `visibility`

One of `public` or `private`.

A private project may still be registered when doing so does not expose confidential information. The registry must never contain secrets, credentials, private client data, or sensitive implementation details.

### `purpose`

One or more reasons the project exists. Examples:

- `technical-portfolio`
- `capability-proof`
- `benchmarking`
- `sales-demo`
- `upwork`
- `research`
- `product`
- `learning`

Purpose values are descriptive and may expand without changing the core family taxonomy.

### `stack`

Primary technologies used by the project. Keep values concise and lowercase where practical.

### `featured`

Boolean. `true` means the project is eligible for curated public surfaces. It does **not** guarantee that it will be pinned or shown everywhere.

### `repository`

Canonical repository URL. Repositories may live under `VionWorks`, `AlexiVion`, another owned organization, or an external collaboration. Registration does not require repository migration.

### `live_demo`

Public demo URL, or `null` when none exists.

## Optional fields

Projects may add the following when useful:

```yaml
owner: AlexiVion
created: 2026-09-13
updated: 2026-09-13
topics:
  - portfolio
  - rag
notes: >-
  Short registry-level note.
```

Do not add project-specific operational configuration to registry files. Application configuration belongs in the project repository.

## Invariants

1. Every registered project has exactly one project file.
2. Every `id` is unique and permanent.
3. Every `slug` is unique within the registry.
4. A repository may be referenced by only one canonical project entry unless an explicit exception is documented.
5. Project IDs are not embedded in repository names.
6. Registry metadata describes projects; it does not replace their technical documentation.
7. Moving a repository does not change the project ID.
8. Archiving a project does not free its ID for reuse.
