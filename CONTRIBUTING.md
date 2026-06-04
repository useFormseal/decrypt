# Contributing to formseal-decrypt

Thanks for your interest in contributing! Contributions of all kinds are welcome — bug fixes, new features, docs, and more.

---

## Table of contents

- [Getting started](#getting-started)
- [Project structure](#project-structure)
- [Versioning](#versioning)
- [Code style](#code-style)
- [Adding new output formats](#adding-new-output-formats)
- [Submitting changes](#submitting-changes)
- [Testing](#testing)
- [Reporting issues](#reporting-issues)
- [Security](#security)

---

## Getting started

1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/useFormseal/decrypt.git
   cd decrypt
   ```

2. Install in development mode using `pipx` (recommended) or `pip`:
   ```bash
   pipx install -e .
   ```

3. Verify it works:
   ```bash
   fsd
   ```

> **Note:** Always use `pipx install -e .` for local dev — it gives you an isolated environment and the version header will display correctly from source.

---

## Project structure

```
formseal-decrypt/
├── fsd/
│   ├── cli.py               # Entry point, command dispatch
│   ├── __main__.py          # python -m fsd support
│   ├── ui/                  # Terminal output helpers (styles, headers, bodies)
│   ├── commands/            # CLI commands (flat: connect, decrypt, status, disconnect)
│   ├── helpers/             # Aliases, errors
│   ├── formats/             # Output format handlers (jsonl, csv, json, md)
│   └── security/            # Key storage (keychain)
├── docs/                    # Documentation
├── .github/                 # GitHub workflows, issue templates
├── pyproject.toml           # Package config
└── version.txt              # Version (single source of truth)
```

---

## Versioning

The version string lives in **`version.txt`** and is the single source of truth. The publish workflow reads it and injects it into the code at build time.

1. Update `version.txt` with your proposed version (e.g., `0.2.0`)
2. The GitHub Actions workflow will automatically inject this into:
   - `fsd/commands/version.py`
   - `pyproject.toml`

---

## Code style

- No comments unless absolutely necessary
- Follow existing patterns in the codebase
- Keep it simple

---

## Adding new output formats

To add a new output format:

1. Create `fsd/formats/{format_name}.py` with a class inheriting from `Formatter`
2. Define `name` and `extension` class attributes
3. Implement `write(data, path)` method
4. Register in `fsd/formats/__init__.py`

---

## Submitting changes

1. Create a branch for your changes:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make your changes and commit with a descriptive message:
   ```bash
   git commit -m "description of your changes"
   ```

3. Push and submit a pull request:
   ```bash
   git push origin feature/my-feature
   ```

---

## Testing

Test manually:
```bash
fsd connect source:test.jsonl destination:. private-key:testkey
fsd decrypt
```

---

## Reporting issues

Report bugs via [GitHub Issues](https://github.com/useFormseal/decrypt/issues/new).

Please include:
- Steps to reproduce
- Expected vs actual behavior
- Your OS and Python version

---

## Security

If you find a security vulnerability, please report it privately via GitHub Security Advisories.

**Do NOT** open a public issue for security vulnerabilities.

