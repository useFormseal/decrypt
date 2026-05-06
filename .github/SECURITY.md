# Security Policy

## Supported versions

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |


## Reporting vulnerabilities

If you find a security vulnerability, please report it privately to allow time for a fix before public disclosure.

**Do NOT** open a public GitHub issue for security vulnerabilities.

### How to report

**GitHub Security Advisories**: Use the "Report a vulnerability" button on this repo's `Security` tab

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact

### Response timeline

- **Acknowledgment**: Best effort (typically within a few days)
- **Assessment**: Best effort based on availability
- **Fix timeline**: Depends on severity and maintainer bandwidth

---

## Credential storage

formseal-decrypt stores sensitive data (private key) in your operating system's secure credential storage:

| OS | Storage location |
|---|------------------|
| Windows | Credential Manager |
| macOS | Keychain |
| Linux | Secret Service API (libsecret) |

### Why OS keychain?

- **Encrypted at rest**: Most operating systems protect stored credentials using OS-level encryption tied to your user account
- **Access controlled**: Requires your user account to access
- **Managed by OS**: Leverages built-in security features

### Fallback behavior

If the OS keychain is unavailable, the private key is stored in base64-encoded JSON at:

```
~/.config/formseal-decrypt/secrets.json
```

:warning: **This fallback is NOT secure.** Base64 encoding is not encryption. Any process with access to this file can read the credentials.

This mode should only be used in environments where secure credential storage (keyring) is unavailable.

---

## What gets stored

| Data | Stored As | Location |
|------|-----------|----------|
| Private Key | Encrypted | OS Keychain (preferred) or secrets.json |
| Source path | Plaintext | config.json |
| Destination dir | Plaintext | config.json |
| Output format | Plaintext | config.json |

---

## Security considerations

- **Key visibility**: `fsd status` masks the key location, not the key itself
- **No telemetry**: The tool does not send usage data, analytics, or logs externally
- **Local operation**: All decryption happens locally on your machine

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

---

## Best practices

1. **Keep your private key secret** — never share it
2. **Use `fsd disconnect`** when done, especially on shared machines
3. **Store decrypted output securely** — it contains plain form data

---

## Clearing credentials

```bash
fsd disconnect
```

This deletes:
- Private key from OS Keychain
- Configuration file (`config.json`)

Decrypted messages are **NOT** affected.