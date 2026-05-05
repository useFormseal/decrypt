# general/aliases.py
# Command aliases

ALIASES = {
    "-s": "status",
    "-c": "connect",
    "-d": "decrypt",
}


def resolve(args):
    if not args:
        return args

    resolved = []
    for arg in args:
        if arg in ALIASES:
            resolved.append(ALIASES[arg])
        else:
            resolved.append(arg)
    return resolved