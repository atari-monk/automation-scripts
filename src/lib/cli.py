from collections.abc import Mapping, Sequence


def require_args(argv: list[str], n: int, usage: str) -> list[str]:
    if len(argv) < n:
        raise SystemExit(usage)
    return argv


def extract_flags(
    argv: Sequence[str],
    specs: Mapping[str, tuple[str, ...]],
) -> tuple[dict[str, bool], list[str]]:
    flags: dict[str, bool] = {name: False for name in specs}
    alias_to_name: dict[str, str] = {
        alias: name for name, aliases in specs.items() for alias in aliases
    }

    remaining: list[str] = []
    for arg in argv:
        name = alias_to_name.get(arg)
        if name is not None:
            flags[name] = True
        else:
            remaining.append(arg)

    return flags, remaining