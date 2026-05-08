# How it works

---

## The flow

```
Browser (formseal-embed)
       │
       ▼ (encrypted submissions)
  Your server (POST endpoint)
       │
       ▼ (ciphertext storage)
  fsf fetch (download ciphertexts)
       │
       ▼ (formseal.ct.jsonl)
  fsd decrypt (decrypt locally)
       │
       ▼ (formseal.decrypted.jsonl/json)
  You (read submissions)
```

1. formseal-embed encrypts form submissions in the browser
2. Ciphertexts are stored at your endpoint (prefixed `formseal.`)
3. fsf fetches ciphertexts from your storage backend
4. fsd decrypts locally using your private key

---

## What fsd does

- Reads ciphertexts from your source file
- Decrypts each one using your private key (X25519 sealed box)
- Writes decrypted JSON to your destination directory
- Supports multiple output formats (JSON Lines, JSON)
- Skips invalid ciphertexts automatically
- Never sends your private key anywhere

---

## What fsd does NOT do

- Never fetches data from any server (that's fsf's job)
- Never stores your private key in plaintext
- Never sends data to external servers
- Never requires network access to decrypt

---

## Output formats

### JSON Lines (default)

One JSON object per line — great for streaming and processing:

```json
{"version": "fse.v1.0", "origin": "contact-form", "id": "uuid", "submitted_at": "2024-01-15T10:30:00Z", "data": {"name": "John"}}
{"version": "fse.v1.0", "origin": "contact-form", "id": "uuid", "submitted_at": "2024-01-15T10:31:00Z", "data": {"name": "Jane"}}
```

### JSON

Pretty-printed JSON array — great for reading and debugging:

```json
[
  {
    "version": "fse.v1.0",
    "origin": "contact-form",
    "id": "uuid",
    "submitted_at": "2024-01-15T10:30:00Z",
    "data": {
      "name": "John",
      "email": "john@example.com"
    }
  }
]
```

---

## Payload structure

Each decrypted submission follows this schema:

```json
{
  "version": "fse.v1.0",
  "origin": "contact-form",
  "id": "uuid",
  "submitted_at": "2024-01-15T10:30:00Z",
  "data": {
    "field1": "value1",
    "field2": "value2"
  }
}
```

See [Deployment → Versioning](versioning.md) for version details.