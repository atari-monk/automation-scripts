import sys
from pathlib import Path

from lib.cli import require_args
from lib.logger import get_logger

LOG_FORMAT = "%(asctime)s %(message)s"


def main():
    logs_dir = Path.home() / "atari-monk/logs"
    args = require_args(sys.argv[1:], 2, 'Usage: log.py log_name "text"')
    log = get_logger("atari-monk-note", logs_dir / (args[0] + ".log"), LOG_FORMAT)
    log.info(args[1])


if __name__ == "__main__":
    main()
