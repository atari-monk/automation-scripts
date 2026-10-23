import os
import subprocess
from dataclasses import dataclass
from typing import List


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


def validate_video_data(data: VideoData) -> None:
    if not data.id:
        raise ValueError("id required")
    if not data.name:
        raise ValueError("name required")
    if not data.tags:
        raise ValueError("tags required")


def build_text(data: VideoData) -> str:
    return f"{data.id} | {data.name} | {data.tags}"


def build_args(script: str, text: str) -> List[str]:
    return [script, "yt-db.log", text]


def run_script(args: List[str]) -> None:
    subprocess.run(["python3", *args], check=True)


def main() -> None:
    script = get_script_path()
    data = prompt_video_data()
    try:
        validate_video_data(data)
    except ValueError as e:
        raise SystemExit(f"{e}")
    text = build_text(data)
    args = build_args(script, text)
    run_script(args)


if __name__ == "__main__":
    main()