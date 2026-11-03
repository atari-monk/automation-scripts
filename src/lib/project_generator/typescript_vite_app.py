from logging import Logger
from pathlib import Path

from lib.project_generator.config import ProjectConfig, create_docs, create_project_configs, create_project_files, create_prompt, set_package_meta


CONFIGS : list[str] = [  
    ".gitignore",
    "index.html",
    "package.json",
    "tsconfig.json"]


SRC : list[str] = [  
    "main.ts",
    "style.css"]


PUBLIC : list[str] = [  
    "favicon.svg"]


def create_ts_vite_app(config: ProjectConfig, log: Logger):
    create_project_configs(config.paths, CONFIGS, log)
    set_package_meta(config, log)
    create_project_files(config.paths, Path("src"), SRC,  log)
    create_project_files(config.paths, Path("public"), PUBLIC, log)
    create_docs(config.paths.target, log)
    create_prompt(config.paths.target, log)
