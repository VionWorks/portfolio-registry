# Project status lifecycle

Every registered project has exactly one status.

## `idea`

The project is recognized but has not yet been scoped enough to start implementation.

## `planning`

Scope, architecture, brief, research question, or delivery plan is being defined.

## `building`

Active implementation is in progress.

## `qa`

Core implementation is complete and the project is being tested, reviewed, polished, documented, or prepared for release.

## `published`

The project is in a presentable state and may be shown publicly or used as professional evidence.

`published` does not mean development has ended. A published project may continue to evolve.

## `archived`

The project is intentionally inactive, superseded, abandoned, or preserved only for historical reference.

Archived IDs are permanent and must never be reused.

## Typical transitions

```text
idea -> planning -> building -> qa -> published
                    |               |
                    +-------------> archived

published -> building
published -> archived
```

Status describes lifecycle state, not quality. A project should only be marked `published` when its repository and documentation are coherent enough to represent VionWorks professionally.
