from logging import Logger
from pathlib import Path

from lib.file_system import create_file_and_log, create_folder_and_log


def create_docs(project_path: Path, log: Logger):
    create_folder_and_log(project_path, "docs", log)
    create_file_and_log(project_path / "docs", "_config.yml", "title: ", log)


def create_prompt(project_path: Path, log: Logger):
    create_folder_and_log(project_path, "prompt", log)
    create_file_and_log(project_path / "prompt", "prompt.md", "", log)
