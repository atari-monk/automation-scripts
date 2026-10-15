## Cli

`lib/cli.py`

- provide `def require_args(argv: list[str], n: int, usage: str) -> list[str]:`
  - make sure there is n args
  - if not raise SystemExit with usage message
