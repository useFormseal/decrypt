# Documentation

Welcome to the formseal-decrypt documentation.

## Quick links

| Guide | Description |
|-------|-------------|
| [Getting Started](./getting-started.md) | Installation and first-time setup |
| [Commands Reference](./reference/commands.md) | All available commands |
| [Configuration](./deployment/configuration.md) | Config files and storage |
| [Troubleshooting](./troubleshooting.md) | Common issues and solutions |

## For developers

| Guide | Description |
|-------|-------------|
| [Concepts → How it works](./concepts/how-it-works.md) | How decryption works |
| [Concepts → Security](./concepts/security.md) | Security model and guarantees |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Contributing guide |
| [SECURITY.md](../.github/SECURITY.md) | Security policy |

## What is formseal-decrypt?

formseal-decrypt is a CLI tool that decrypts form submissions locally. Use it together with [formseal-fetch](https://github.com/useFormseal/fetch) — the tool that downloads encrypted ciphertexts from your storage backend.

## Workflow

```
Browser (formseal-embed)
       │
       ▼ (encrypted submissions)
  Your server (POST endpoint)
       │
       ▼ (ciphertext storage)
  fsf fetch
       │
       ▼ (ciphertexts.jsonl)
  fsd decrypt
       │
       ▼ (decrypted.jsonl/json)
  You
```

## Output model

`fsd decrypt` always writes `formseal.decrypted.jsonl` as the canonical JSONL ledger. Pass `--format` for additional exports:

- **JSON Lines** — one JSON object per line (canonical)
- **JSON** — pretty-printed JSON array
- **CSV** — spreadsheet-compatible table
- **Markdown** — table view, opens in any markdown viewer