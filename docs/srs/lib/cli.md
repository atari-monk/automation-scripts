## Cli

`lib/cli.py`

### require_args

- provide `def require_args(argv: list[str], n: int, usage: str) -> list[str]:`
  - make sure there is n args
  - if not raise SystemExit with usage message

### extract_flags

- provide

```py
def extract_flags(
    argv: Sequence[str],
    specs: Mapping[str, tuple[str, ...]],
) -> tuple[dict[str, bool], list[str]]:
```

- pull boolean flags out of argv
- args:
  - argv: raw argument list (e.g. sys.argv[1:])
  - specs: canonical flag name -> tuple of aliases
    - e.g. {"start": ("-s", "--start"), "end": ("-e", "--end")}
- returns:
  - (flags, remaining) where flags maps each canonical name to True if
    any of its aliases appeared in argv, and remaining is argv with
    all recognized flags removed (order preserved)
