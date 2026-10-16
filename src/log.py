import sys
from pathlib import Path

from lib.cli import require_args, extract_flags
from lib.logger import get_logger

LOG_FORMAT = "%(asctime)s %(message)s"

MARKERS = {
    "start": "[START] ",
    "end":   "[END]   ",
}


def main():
    flags, argv = extract_flags(
        sys.argv[1:],
        {"start": ("-s", "--start"), "end": ("-e", "--end")},
    )

    marker = next((MARKERS[k] for k, v in flags.items() if v), "")

    args = require_args(argv, 2, 'Usage: log.py log_name "text" [-s|-e]')

    logs_dir = Path.home() / "atari-monk/logs"
    log = get_logger("atari-monk-note", logs_dir / (args[0] + ".log"), LOG_FORMAT)
    log.info(marker + args[1])


if __name__ == "__main__":
    main()