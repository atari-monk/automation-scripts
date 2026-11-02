import os
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class VideoData:
    category: str
    name: str
    id: str


@dataclass(frozen=True)
class LogPath:
    folder: str
    name: str

    def build(self) -> str:
        return str(Path(self.folder) / self.name)


def get_script_path() -> str:
    home = os.environ.get("HOME", "")
    return str(
        Path(home)
        / "atari-monk"
        / "project"
        / "automation-scripts"
        / "src"
        / "log.py"
    )


def prompt_video_data() -> VideoData:
    category = input("category: ").strip()
    name = input("name: ").strip()
    video_id = input("id: ").strip()

    return VideoData(
        category=category,
        name=name,
        id=video_id,
    )


def prompt_log_path() -> LogPath:
    folder = input("log folder [yt]: ").strip() or "yt"
    name = input("log name [video]: ").strip() or "video"

    return LogPath(
        folder=folder,
        name=name,
    )

def validate_video_data(data: VideoData) -> None:
    if not data.category:
        raise ValueError("category required")

    if not data.name:
        raise ValueError("name required")

    if not data.id:
        raise ValueError("id required")


def validate_log_path(log_path: LogPath) -> None:
    if not log_path.folder:
        raise ValueError("log folder required")

    if not log_path.name:
        raise ValueError("log name required")


def build_text(data: VideoData) -> str:
    return f"{data.category} | {data.name} | {data.id}"


def build_args(script: str, log_path: str, text: str) -> list[str]:
    return [
        script,
        log_path,
        text,
    ]


def run_script(args: list[str]) -> None:
    subprocess.run(
        ["python3", *args],
        check=True,
    )


def main() -> None:
    script = get_script_path()

    try:
        data = prompt_video_data()
        validate_video_data(data)

        log_path = prompt_log_path()
        validate_log_path(log_path)

    except ValueError as error:
        raise SystemExit(str(error)) from error

    text = build_text(data)
    args = build_args(
        script,
        log_path.build(),
        text,
    )

    run_script(args)


if __name__ == "__main__":
    main()