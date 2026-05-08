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

Configure source, destination, format, and private key.

```bash
fsd connect [field:value]...
```

**Arguments:**

| Argument | Description |
|----------|-------------|
| `source:<path>` | Path to ciphertext file (auto-appends .jsonl if missing) |
| `destination:<path>` | Directory for decrypted output |
| `format:<name>` | Output format: `jsonl` or `json` |
| `private-key:<key>` | Your private key from formseal-embed |

**Examples:**

```bash
# Interactive mode — you'll be prompted for all required values
fsd connect

# Non-interactive — all values provided via arguments
fsd connect source:ciphertexts.jsonl destination:. private-key:YOUR_KEY format:json
```

Press `Ctrl+C` at any prompt to cancel.

---

### decrypt

Decrypt ciphertexts from your source file.

```bash
fsd decrypt
```

Decrypts all ciphertexts and writes to `formseal.decrypted.{jsonl|json}` in your destination directory.

**What happens:**

1. Loads configuration and private key
2. Reads source file line by line
3. Decrypts each ciphertext using NaCl sealed box
4. Writes output using your chosen format

**Output shows:**
- Number of processed ciphertexts
- Number successfully decrypted
- Number that failed (wrong key or malformed)

---

### status

Show current configuration and credential storage.

```bash
fsd status
```

**Output includes:**
- Source file path
- Destination directory
- Output format
- Private key storage location (OS Keychain or Config File)

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
fsd version
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

### --about

Show project information.

```bash
fsd --about
```

---

## Examples

### Full workflow

```bash
# Configure
fsd connect source:ciphertexts.jsonl destination:. private-key:YOUR_KEY format:jsonl

# Decrypt
fsd decrypt

# Check status
fsd status

# Clear credentials when done
fsd disconnect
```

### Change format

```bash
# Disconnect and reconnect with different format
fsd disconnect
fsd connect source:ciphertexts.jsonl destination:. private-key:YOUR_KEY format:json
fsd decrypt
```