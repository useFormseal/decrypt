# Documentation

Welcome to the formseal-decrypt documentation.

| Guide | Description |
|-------|-------------|
| [Getting Started](./0. getting-started.md) | Installation and first-time setup |
| [Commands Reference](./1. commands.md) | All available commands |
| [Configuration](./2. configuration.md) | Config files and credential storage |
| [How it works](./3. how-it-works.md) | Decryption flow and output formats |
| [Output formats](./4. output-formats.md) | Format specs, overwrite policy, CSV safety |
| [Security](./5. security.md) | Security model, key storage, and threat model |
| [Versioning](./6. versioning.md) | Payload version schema |
| [Troubleshooting](./7. troubleshooting.md) | Common issues and solutions |
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
        ▼ (formseal.decrypted.jsonl + optional exports)
   You
```

`fsd decrypt` always writes `formseal.decrypted.jsonl` as the canonical JSONL ledger. Pass `--format` for additional exports. See [Output formats](./4. output-formats.md) for details.