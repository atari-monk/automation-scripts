from dataclasses import dataclass
from pathlib import Path
from logging import Logger
import shutil


@dataclass
class FileSystemResult:
    path: Path
    created: bool


def log_file_system_result(result: FileSystemResult, logger: Logger) -> None:
    if result.created:
        logger.info(f"Created: {result.path}")
    else:
        logger.debug(f"Already exists: {result.path}")


def create_folder(parent_path: Path, folder_name: str) -> FileSystemResult:
    path = parent_path / folder_name
    try:
        path.mkdir(parents=True)
        return FileSystemResult(path=path, created=True)
    except FileExistsError as exc:
        if not path.is_dir():
            raise NotADirectoryError(f"Path exists but is not a directory: {path}") from exc
        return FileSystemResult(path=path, created=False)


def create_folder_and_log(parent_path: Path, folder_name: str, logger: Logger) -> FileSystemResult:
    result = create_folder(parent_path, folder_name)
    log_file_system_result(result, logger)
    return result


def create_file(
    parent_path: Path,
    file_name: str,
    content: str = "",
) -> FileSystemResult:
    path = parent_path / file_name
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(path, "x", encoding="utf-8") as f:
            f.write(content)
        return FileSystemResult(path=path, created=True)
    except FileExistsError as exc:
        if path.is_dir():
            raise IsADirectoryError(f"Path is a directory: {path}") from exc
        return FileSystemResult(path=path, created=False)


def create_file_and_log(
    parent_path: Path,
    file_name: str,
    content: str,
    logger: Logger,
) -> FileSystemResult:
    result = create_file(parent_path, file_name, content)
    log_file_system_result(result, logger)
    return result


def copy_file_and_log(
    source: Path,
    destination: Path,
    logger: Logger,
) -> bool:
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        with open(source, "rb") as src, open(destination, "xb") as dst:
            shutil.copyfileobj(src, dst)
        logger.info("Copied %s to %s", source, destination)
        return True
    except FileExistsError:
        logger.debug("Already exists, skipped: %s", destination)
        return False
    except FileNotFoundError:
        logger.warning("Source file does not exist: %s", source)
        return False
    except OSError as error:
        logger.warning("Failed to copy %s to %s: %s", source, destination, error)
        return False
