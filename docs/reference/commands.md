# Commands reference

Complete reference for all formseal-decrypt commands.

---

## Usage syntax

```bash
fsd <command> [options] [arguments]
```

---

## Commands

### connect

Configure source, destination, and private key.

```bash
fsd connect [field:value]...
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `source:<path>` | Path to ciphertext file (auto-appends .jsonl if missing) |
| `destination:<path>` | Directory for decrypted output |
| `private-key:<key>` | Your private key from formseal-embed |

**Examples:**

```bash
# Interactive mode — you'll be prompted for all required values
fsd connect

# Non-interactive — all values provided via arguments
fsd connect source:ciphertexts.jsonl destination:. private-key:YOUR_KEY
```

Press `Ctrl+C` at any prompt to cancel.

---

### decrypt

Decrypt ciphertexts from your source file.

```bash
fsd decrypt [--format <name>]
```

Always writes `formseal.decrypted.jsonl` (canonical JSONL ledger). Pass `--format` for an additional export:

```bash
fsd decrypt --format csv
fsd decrypt --format json
fsd decrypt --format md
```

Available formats: `csv`, `jsonl`, `json`, `md` (see `fsd --formats`).

**What happens:**

1. Loads configuration and private key
2. Reads source file line by line
3. Decrypts each ciphertext using NaCl sealed box
4. Always writes canonical JSONL; exports other formats on request

**Output shows:**
- Number of processed ciphertexts
- Number successfully decrypted
- Number that failed (wrong key or malformed)

---

### status

Show current configuration and decryption status.

```bash
fsd status
```

**Output includes:**
- Source file path
- Destination directory
- Key storage location
- Source entry count
- Decrypted entry count
- Last decrypt timestamp

---

### disconnect

Clear all credentials and configuration.

```bash
fsd disconnect
fsd disconnect --wipe
```

**What it removes:**

- Private key (from OS Keychain or secrets.json)
- Configuration file (`config.json`)

**What it does NOT remove (disconnect only):**

- Decrypted files in your destination folder

**--wipe flag:**

```bash
fsd disconnect --wipe
```

This removes everything above PLUS all decrypted files in your destination directory.

---

### --formats

List available export formats.

```bash
fsd --formats
```

---

### --help

Show help information.

```bash
fsd --help
```

---

### --version

Show version number.

```bash
fsd --version
```

---

### --aliases

Show shorthand aliases.

```bash
fsd --aliases
```

Lists all available shorthand flags:

| Short | Canonical |
|-------|-----------|
| `-s` | `status` |
| `-c` | `connect` |
| `-d` | `decrypt` |

---

### No-argument

Show project information.

```bash
fsd
```

---

## Examples

### Full workflow

```bash
# Configure
fsd connect source:ciphertexts.jsonl destination:. private-key:YOUR_KEY

# Decrypt (always writes canonical JSONL + optional export)
fsd decrypt --format csv

# Check status
fsd status

# Clear credentials when done
fsd disconnect
```

### Change export format

```bash
# Just pass --format to decrypt — no reconnect needed
fsd decrypt --format json
fsd decrypt --format md
```