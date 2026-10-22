import sys
from pathlib import Path

from lib.logger import get_logger
from lib.cli import require_args
from lib.file_system import create_folder_and_log
from lib.typescript_library import create_ts_lib


TEMPLATES = {
    "tslib": create_ts_lib,
}


def main():
    args = require_args(sys.argv[1:], 2, 'Usage: create_proj.py proj_name template_name proj_description')
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

    TEMPLATES[template_name](result.path, proj_name, proj_description, log)

if __name__ == "__main__":
    main()