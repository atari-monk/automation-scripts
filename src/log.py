import sys
from pathlib import Path

from lib.cli import require_args, extract_flags
from lib.logger import get_logger

LOG_FORMAT = "%(asctime)s %(message)s"

MARKERS = {
    "start": "[START] ",
    "end": "[END]   ",
}

ALIASES = {"start": ("-s", "--start"), "end": ("-e", "--end")}


def main() -> None:
    flags, argv = extract_flags(sys.argv[1:], ALIASES)

    marker = next((MARKERS[k] for k, v in flags.items() if v), "")

    args = require_args(argv, 2, 'Usage: log.py log_path "text" [-s|-e]')
    log_path = args[0]
    text = args[1]

    logs_dir = Path.home() / "atari-monk/logs"
    log_file = logs_dir / (log_path + ".log")
    log_file.parent.mkdir(parents=True, exist_ok=True)

    log = get_logger("atari-monk-log", log_file, LOG_FORMAT)
    log.info(marker + text)


if __name__ == "__main__":
    main()