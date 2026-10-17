## Logger

`src/lib/logger.py`

- provide

```py
def get_logger(
        name: str,
        log_path: Path,
        fmt: str = DEFAULT_FORMAT) -> Logger:
```

- set default value for log format to "%(asctime)s [%(levelname)s] %(name)s: %(message)s"

- provide `def configure_logger(logger: Logger) -> None:`
  - set which level will be ignored
  - avoid duplicate messages via root logger by not propagate

- provide `def clear_logger_handlers(logger: Logger) -> None:`
  - clear pre-existing handlers to prevent duplicate output on re-calls

- provide `def build_logger_formatter(fmt: str) -> Formatter:`
  - allowing to set any log format

- provide `def add_logger_file_handler(logger: Logger, log_path: Path, formatter: Formatter) -> None:`

- provide `def add_logger_console_handler(logger: Logger, formatter: Formatter) -> None:`
