# Getting started

Install formseal-decrypt and start decrypting form submissions.

---

## Installation

### From PyPI (recommended)

```bash
pip install formseal-decrypt
```

Or with pipx:

```bash
pipx install formseal-decrypt
```

### From source

```bash
git clone https://github.com/useFormseal/decrypt.git
cd decrypt
pip install -e .
```

### Verify installation

```bash
fsd
```

---

## Quick start

### Step 1: Connect to your ciphertexts

```bash
fsd connect
```

You'll be prompted for:
- **Source file** — your ciphertexts (e.g., `formseal.ct.jsonl`)
- **Destination directory** — where decrypted files go
- **Private key** — your private key from formseal-embed setup

You can also provide everything non-interactively:

```bash
fsd connect source:ciphertexts.jsonl destination:. private-key:YOUR_KEY
```

### Step 2: Decrypt

```bash
fsd decrypt
```

This decrypts all ciphertexts and always writes `formseal.decrypted.jsonl` (canonical ledger). Pass `--format` for an additional export:

```bash
fsd decrypt --format csv
fsd decrypt --format json
fsd decrypt --format md
```

### Step 3: Check status

```bash
fsd status
```

Shows your source, destination, key location, entry counts, and last decrypt timestamp.

---

## Next steps

- See [Commands reference](./reference/commands.md) for all available commands
- Read [Configuration](./deployment/configuration.md) to understand how credentials are stored
- Check [Troubleshooting](./troubleshooting.md) if you encounter issues