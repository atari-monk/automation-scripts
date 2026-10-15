from logging import DEBUG, FileHandler, Formatter, Logger, StreamHandler, getLogger
from pathlib import Path

DEFAULT_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"


def get_logger(name: str, log_path: Path, fmt: str = DEFAULT_FORMAT) -> Logger:
    logger = getLogger(name)
    clear_logger_handlers(logger)
    configure_logger(logger)
    formatter = build_logger_formatter(fmt)
    add_logger_file_handler(logger, log_path, formatter)
    add_logger_console_handler(logger, formatter)
    return logger


def configure_logger(logger: Logger) -> None:
    logger.setLevel(DEBUG)
    logger.propagate = False


def clear_logger_handlers(logger: Logger) -> None:
    for h in list(logger.handlers):
        logger.removeHandler(h)
        h.close()


def build_logger_formatter(fmt: str) -> Formatter:
    return Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")


def add_logger_file_handler(
    logger: Logger, log_path: Path, formatter: Formatter
) -> None:
    handler = FileHandler(log_path, mode="a", encoding="utf-8", delay=True)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def add_logger_console_handler(logger: Logger, formatter: Formatter) -> None:
    handler = StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
