from logging import Logger
from pathlib import Path

from lib.project_generator.config import ProjectConfig, create_docs, create_project_configs, create_project_files, create_prompt, set_package_meta


CONFIGS : list[str] = [
    "index.html",
    ".gitignore",
    "package.json",
    "tsconfig.json",
    "vite.config.js",
]


SRC : list[str] = [  
    "game/create-game.ts",
    "game/game-loop.ts",
    "game/game-state.ts",
    "game/render-game.ts",
    "game/update-game.ts",
    "main.ts",
    "style.css",
]

PUBLIC : list[str] = [  
    "favicon.png"]


def create_game_app(config: ProjectConfig, log: Logger) -> None:
    create_project_configs(config.paths, CONFIGS, log)
    set_package_meta(config, log)
    create_project_files(config.paths, Path("src"), SRC, log)
    create_docs(config.paths.target, log)
    create_prompt(config.paths.target, log)
