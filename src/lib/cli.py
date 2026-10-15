def require_args(argv: list[str], n: int, usage: str) -> list[str]:
    if len(argv) < n:
        raise SystemExit(usage)
    return argv
