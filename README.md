<p align="center">
  <img src="fsd.png" alt="formseal-decrypt">
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/formseal-decrypt?style=flat&label=pypi&labelColor=1e293b&color=3776ab">
  <img src="https://img.shields.io/github/actions/workflow/status/useFormseal/decrypt/publish.yml">
  <img src="https://img.shields.io/badge/license-MIT-fc8181?style=flat&labelColor=1e293b">
  <img src="https://img.shields.io/badge/formseal-ecosystem-10b981?style=flat&labelColor=1e293b">
</p>

<p align="center">
  Decrypt formseal ciphertexts locally.
</p>

---

formseal-decrypt decrypts form submissions downloaded by formseal-fetch. Nothing is decrypted in transit or on the server — only the holder of the private key can read submissions.

formseal-decrypt is not a hosted service or dashboard. It is a CLI decryption utility.

---

## Installation

**Via pipx (recommended)**

```bash
pipx install formseal-decrypt
```

**Via pip**

```bash
pip install formseal-decrypt
```

---

## Quick start

```bash
fsd connect
fsd decrypt
fsd status
```

---

## How it works

```
Browser (formseal-embed)
       │
       ▼ (encrypted submissions)
 Your server / endpoint
       │
       ▼ (fsf fetch)
 ciphertexts.jsonl ──► Your PC
       │
       ▼ (fsd decrypt)
 formseal.decrypted.jsonl (or .json for pretty output)
```

Your backend stores opaque ciphertext only. `fsf fetch` downloads it. `fsd decrypt` decrypts it offline with your private key.

---

## Commands

| Command | Description |
|---------|-------------|
| `fsd` | Show about / info |
| `fsd connect` | Configure source, destination, private key, and format |
| `fsd decrypt` | Decrypt ciphertexts |
| `fsd status` | Show configuration |
| `fsd disconnect` | Clear credentials |
| `fsd disconnect --wipe` | Clear everything including messages |

Run `fsd --help` for all options.

---

## Output Formats

During `fsd connect`, you can choose the output format:

- **JSON Lines** (`jsonl`) — One JSON object per line
- **JSON** (`json`) — Pretty-printed JSON array

---

## Security

Your private key never leaves your machine. formseal-decrypt:

- Stores credentials in your OS keychain (Windows Credential Manager / macOS Keychain / Linux Secret Service)
- Decrypts locally only
- Sends no telemetry, has no analytics
- Skips already-decrypted messages automatically

---

## Documentation

- [SECURITY.md](./.github/SECURITY.md) — Security policy

---

Please star the repo if you find formseal-decrypt useful.

---

## License

MIT