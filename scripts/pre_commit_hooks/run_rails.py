#!/usr/bin/env python3

import logging
import os
import sys
import pathlib

from typing import Optional
from typing import Sequence

log_format = "%(asctime)s %(levelname)s %(processName)s %(threadName)s %(message)s"

logging.basicConfig(level=logging.DEBUG,
                    format=log_format,
                    datefmt="%Y%m%d %H:%M:%S")
logger = logging.getLogger(__name__)

RUBOCOP_DEFAULT_COMMAND = "--extra-details --display-style-guide --parallel"


def main(argv: Optional[Sequence[str]] = None) -> int:
    logger.debug("argv {}".format(argv))

    os.chdir(argv[1])

    cmd = "rails {}".format(' '.join(argv[2:]))
    logger.debug("cmd {}".format(cmd))

    ret = os.system(cmd)
    if ret != 0:
        ret = -1
    return ret


if __name__ == '__main__':
    exit(main(sys.argv))
