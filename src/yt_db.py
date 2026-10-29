import os
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class VideoData:
    id: str
    name: str
    tags: str


def get_script_path() -> str:
    home = os.environ.get("HOME", "")
    return os.path.join(home, "atari-monk/project/automation-scripts/src/log.py")


def prompt_video_data() -> VideoData:
    video_id = input("id: ").strip()
    name = input("name: ").strip()
    tags = input("tags (comma separated): ").strip()
    return VideoData(id=video_id, name=name, tags=tags)


def prompt_log_path() -> str:
    folder = input("log folder: ").strip()
    log_name = input("log name: ").strip()

    if not folder:
        raise ValueError("log folder required")
    if not log_name:
        raise ValueError("log name required")

    return str(Path(folder) / log_name)


def validate_video_data(data: VideoData) -> None:
    if not data.id:
        raise ValueError("id required")
    if not data.name:
        raise ValueError("name required")
    if not data.tags:
        raise ValueError("tags required")


def build_text(data: VideoData) -> str:
    return f"{data.id} | {data.name} | {data.tags}"


def build_args(script: str, log_path: str, text: str) -> list[str]:
    return [script, log_path, text]


def run_script(args: list[str]) -> None:
    subprocess.run(["python3", *args], check=True)


def main() -> None:
    script = get_script_path()

    try:
        data = prompt_video_data()
        validate_video_data(data)
        log_path = prompt_log_path()
    except ValueError as error:
        raise SystemExit(str(error)) from error

    text = build_text(data)
    args = build_args(script, log_path, text)
    run_script(args)


if __name__ == "__main__":
    main()