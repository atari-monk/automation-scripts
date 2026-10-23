from logging import Logger
from pathlib import Path

from lib.file_system import copy_file_and_log, create_file_and_log, create_folder_and_log
from lib.json_helper import set_package_meta
from lib.project_files import create_docs, create_prompt


BASE_PATH = Path("/home/atari-monk/atari-monk/project")
TYPESCRIPT_LIBRARY_PATH = BASE_PATH / "typescript-library"


def create_src(project_path: Path, log: Logger):
    create_folder_and_log(project_path, "src", log)
    create_file_and_log(project_path / "src", "index.ts", "", log)


def create_configs(project_path: Path, name: str, description: str, log: Logger):
    for file_name in [
        ".gitignore",
        "package.json",
        "README.md",
        "tsconfig.json",
        "tsup.config.ts"
    ]:
        copy_file_and_log(
            TYPESCRIPT_LIBRARY_PATH / file_name,
            project_path / file_name,
            log,
        )

    set_package_meta(project_path / "package.json", name, description, log)


def create_ts_lib(project_path: Path, name: str, description: str, log: Logger):
    create_docs(project_path, log)
    create_prompt(project_path, log)
    create_src(project_path, log)
    create_configs(project_path, name, description, log)
