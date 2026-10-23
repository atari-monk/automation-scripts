from logging import Logger
from pathlib import Path

from lib.file_system import copy_file_and_log
from lib.json_helper import set_package_meta
from lib.project_files import create_docs, create_prompt


BASE_PATH = Path("/home/atari-monk/atari-monk")
TYPESCRIPT_VITE_APP_PATH = BASE_PATH / "project" / "typescript-vite-app"


def create_configs(project_path: Path, name: str, description: str, log: Logger):
    for file_name in [
        ".gitignore",
        "index.html",
        "package.json",
        "tsconfig.json"
    ]:
        copy_file_and_log(
            TYPESCRIPT_VITE_APP_PATH / file_name,
            project_path / file_name,
            log,
        )

    set_package_meta(project_path / "package.json", name, description, log)


def create_src(project_path: Path, log: Logger):
    for file_name in [
        "main.ts",
        "style.css"
    ]:
        copy_file_and_log(
            TYPESCRIPT_VITE_APP_PATH / "src" / file_name,
            project_path / "src" / file_name,
            log,
        )

def create_public(project_path: Path, log: Logger):
    for file_name in [
        "favicon.svg"
    ]:
        copy_file_and_log(
            TYPESCRIPT_VITE_APP_PATH / "public" / file_name,
            project_path / "public" / file_name,
            log,
        )


def create_ts_vite_app(project_path: Path, name: str, description: str, log: Logger):
    create_configs(project_path, name, description, log)
    create_src(project_path, log)
    create_public(project_path, log)
    create_docs(project_path, log)
    create_prompt(project_path, log)
