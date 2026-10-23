import os
import subprocess
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class LogData:
    name: str
    text: str
    flag: Optional[str] = None


def get_script_path() -> str:
    home = os.environ.get("HOME", "")
    return os.path.join(home, "atari-monk/project/automation-scripts/src/log.py")


def prompt_log_data() -> LogData:
    name = input("name: ").strip()
    text = input("text: ").strip()
    flag = input("flag (blank/-s/-e, optional): ").strip()
    return LogData(name=name, text=text, flag=flag or None)


def validate_log_data(data: LogData) -> None:
    if not data.name:
        raise ValueError("name required")
    if not data.text:
        raise ValueError("text required")
    if data.flag and data.flag not in ("-s", "-e"):
        raise ValueError("flag must be blank, -s, or -e")


def build_args(script: str, data: LogData) -> List[str]:
    args = [script, data.name, data.text]
    if data.flag:
        args.append(data.flag)
    return args


def run_script(args: List[str]) -> None:
    subprocess.run(["python3", *args], check=True)


def main() -> None:
    script = get_script_path()
    data = prompt_log_data()
    try:
        validate_log_data(data)
    except ValueError as e:
        raise SystemExit(f"{e}")
    args = build_args(script, data)
    run_script(args)


if __name__ == "__main__":
    main()