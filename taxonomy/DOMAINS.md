# Domains

`domain` is the project's primary broad subject or market area. It is intentionally higher-level than `areas`.

The domain list is controlled but extensible. Add a new domain only when an existing one would materially misclassify the project.

## Initial canonical domains

- `artificial-intelligence`
- `software-engineering`
- `data`
- `developer-tools`
- `hospitality`
- `restaurants`
- `real-estate`
- `healthcare`
- `ecommerce`
- `marketing`
- `automation`
- `finance`
- `education`
- `research`
- `other`

## Domain vs. area

Use one broad `domain` and multiple focused `areas`.

Example:

```yaml
domain: artificial-intelligence
areas:
  - rag
  - information-retrieval
  - evaluation
```

Example:

```yaml
domain: hospitality
areas:
  - web-development
  - direct-booking
  - conversion
```

Do not create a new domain for every niche. Prefer `areas` for fine-grained classification.
