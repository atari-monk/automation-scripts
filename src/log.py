#from pathlib import Path

from lib.hello import hello_world

#from lib.logger import get_logger

#LOG_FORMAT = "%(asctime)s %(message)s"


def main():
    hello_world()
    # get_logger("atari-monk-note", 
    #            Path("/home/atari-monk/atari-monk/logs/test.log"), 
    #            LOG_FORMAT)

if __name__ == "__main__":
    main()