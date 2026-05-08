# Security

---

## Credential storage

formseal-decrypt stores sensitive data in your operating system's secure credential storage:

| OS | Storage location |
|---|------------------|
| Windows | Credential Manager |
| macOS | Keychain |
| Linux | Secret Service API (libsecret) |

### OS keychain

This is the preferred and secure method:
- Credentials are encrypted at rest by the OS
- Access requires your user account
- Managed by the OS — leverages built-in security features

### Fallback behavior

If the OS keychain is unavailable, the private key is stored in base64-encoded JSON at:

```
~/.config/formseal-decrypt/secrets.json
```

**This fallback is NOT secure.** Base64 encoding is not encryption. Any process with access to this file can read the credentials.

This mode should only be used in environments where secure credential storage (keyring) is unavailable.

---

## What gets stored

| Data | Stored As | Location |
|------|-----------|----------|
| Private Key | Encrypted | OS Keychain (preferred) or secrets.json |
| Source path | Plaintext | config.json |
| Destination directory | Plaintext | config.json |
| Output format | Plaintext | config.json |

---

## Security guarantees

formseal-decrypt:

- **Never sends your private key anywhere** — decryption happens entirely on your machine
- **Never connects to external servers** — works offline
- **No telemetry or analytics** — no network calls during operation
- **Stores credentials securely** — uses OS keychain when available

---

## What to protect

### Your private key

If your private key is exposed, an attacker can decrypt all past and future submissions.

**Best practices:**
- Never commit the private key to version control
- Store it securely — use the OS keychain (default)
- Reconnect with `fsd disconnect` when done, especially on shared machines
- If you suspect exposure, generate a new key pair and update your formseal-embed config

### Decrypted output

The decrypted JSON contains your form submission data. Protect it like any other sensitive data:
- Don't commit to version control
- Store in a secure location
- Delete when no longer needed

---

## Threat model

formseal-decrypt is a local CLI tool. It assumes:

- The system is trusted by the user
- The user account is not compromised
- The tool is not exposed to untrusted remote input

It does **NOT** protect against:
- Malware on the system
- Other local users with access to your files
- Physical access to the machine
- Compromised private key

---

## Clearing credentials

```bash
fsd disconnect
```

This deletes:
- Private key from OS Keychain
- Configuration file (`config.json`)
- Fallback secrets file (if exists)

Decrypted message files are **NOT** affected.

To also delete decrypted messages:

```bash
fsd disconnect --wipe
```

---

## Verifying keychain storage

Run `fsd status` — if "Private Key Location" shows "OS Keychain", your credentials are stored securely.