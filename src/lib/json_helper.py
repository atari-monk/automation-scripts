import json
from logging import Logger
from pathlib import Path


def set_package_meta(path: Path, name: str, description: str, log: Logger) -> None:
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