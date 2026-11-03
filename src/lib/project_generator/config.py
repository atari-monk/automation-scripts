from logging import Logger
from pathlib import Path
import json
from dataclasses import dataclass

from lib.file_system import copy_file_and_log, create_file_and_log, create_folder_and_log


BASE_PATH = Path("/home/atari-monk/atari-monk")
PROJECT_PATH = BASE_PATH / "project"
TYPESCRIPT_LIBRARY_PATH = PROJECT_PATH / "typescript-library"
TYPESCRIPT_VITE_APP_PATH = PROJECT_PATH / "typescript-vite-app"
GAME_APP_PATH = PROJECT_PATH / "game"


@dataclass
class ProjectPath:
    source: Path
    target: Path


@dataclass
class ProjectInfo:
    name: str
    description: str


@dataclass
class ProjectConfig:
    paths: ProjectPath
    info: ProjectInfo


def create_project_configs(config: ProjectPath, files: list[str], log: Logger) -> None:
    for file_name in files:
        copy_file_and_log(
            config.source / file_name,
            config.target / file_name,
            log,
        )


def create_project_files(config: ProjectPath, path: Path, files: list[str], log: Logger) -> None:
    for file_name in files:
        copy_file_and_log(
            config.source / path / file_name,
            config.target / path / file_name,
            log,
        )


def set_package_meta(config: ProjectConfig, log: Logger) -> None:
    path = config.paths.target / "package.json"
    name = config.info.name
    description = config.info.description
    pkg = json.loads(path.read_text(encoding="utf-8"))
    pkg["name"] = name
    pkg["description"] = description
    path.write_text(
        json.dumps(pkg, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    log.info(
        "%s: set name to %s and description to %s",
        path.name,
        name,
        description,
    )


def create_docs(project_path: Path, log: Logger):
    create_folder_and_log(project_path, "docs", log)
    create_file_and_log(project_path / "docs", "_config.yml", "title: ", log)


def create_prompt(project_path: Path, log: Logger):
    create_folder_and_log(project_path, "prompt", log)
    create_file_and_log(project_path / "prompt", "prompt.md", "", log)
