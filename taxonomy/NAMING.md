# Naming conventions

Repository names should remain human-readable, durable, and independent from internal project IDs.

## General rules

Use lowercase kebab-case:

```text
rag-architecture-lab
hospitality-casa-luma
agent-architecture-lab
```

Avoid:

```text
project-final
new-project
hotel-demo-1
test2
website-v3
```

Project IDs such as `TECH-001` belong in registry metadata, not in repository names.

## TECH repositories

Prefer capability-oriented names that make the technical subject obvious.

Pattern examples:

```text
rag-architecture-lab
agent-architecture-lab
vector-search-lab
llm-evaluation-lab
```

## DEMO repositories

Prefer a broad vertical or problem area followed by the concept name.

Pattern:

```text
<vertical>-<project-name>
```

Examples:

```text
hospitality-casa-luma
dental-nova
restaurant-sora
realestate-haven
```

## PROD repositories

Use the actual product or service name. Do not rename a real product simply to fit the portfolio taxonomy.

## RES repositories

Prefer names based on the research question, method, benchmark, or reproduction target.

## PLAY repositories

Small experiments should normally be grouped into a shared playground instead of generating standalone repositories. A PLAY item receives its own repository only when it has enough independent value or scope to justify one.

## Renaming policy

Repository names may change when presentation materially improves, but the registry `id` remains permanent. Update `slug` and `repository` metadata when a rename occurs.
