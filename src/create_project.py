from dataclasses import dataclass
from logging import Logger
import sys
from pathlib import Path
from typing import Callable

from lib.logger import get_logger
from lib.cli import require_args
from lib.file_system import create_folder_and_log
from lib.project_generator.config import GAME_APP_PATH, TYPESCRIPT_LIBRARY_PATH, TYPESCRIPT_VITE_APP_PATH, ProjectConfig, ProjectInfo, ProjectPath
from lib.project_generator.game_app import create_game_app
from lib.project_generator.typescript_library import create_ts_lib
from lib.project_generator.typescript_vite_app import create_ts_vite_app


@dataclass
class ProjectTemplate:
    source: Path
    function:  Callable[[ProjectConfig, Logger], None]


TEMPLATES : dict[str, ProjectTemplate] = {
    "tslib": ProjectTemplate(source=TYPESCRIPT_LIBRARY_PATH, function=create_ts_lib),
    "tsviteapp": ProjectTemplate(source=TYPESCRIPT_VITE_APP_PATH, function=create_ts_vite_app),
    "gameapp": ProjectTemplate(source=GAME_APP_PATH, function=create_game_app)
}


def main():
    args = require_args(sys.argv[1:], 2, 'Usage: create_proj.py proj_name template_name (tslib, tsviteapp) proj_description')
    proj_name, template_name, proj_description = args

    log_dir = Path.home() / "atari-monk/logs"
    log = get_logger("create-project", log_dir / "create-project.log")

    if template_name not in TEMPLATES:
        log.error(f"Unknown template: {template_name}. Known: {list(TEMPLATES)}")
        sys.exit(1)
    
    projects_root = Path.home() / "atari-monk/project"    
    log.info(f"Creating project {proj_name} using {template_name} template")
    result = create_folder_and_log(projects_root, proj_name, log)
    if not result.created:
        log.warning(f"Project folder already exists: {result.path}")
        return

    template = TEMPLATES[template_name]

    config = ProjectConfig(
        ProjectPath(source= template.source, target=result.path),
        ProjectInfo(name=proj_name, description=proj_description))

    template.function(config, log)

if __name__ == "__main__":
    main()