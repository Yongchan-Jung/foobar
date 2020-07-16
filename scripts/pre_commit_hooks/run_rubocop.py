#!/usr/bin/env python3

import logging
import os
import sys
import pathlib

from typing import Optional
from typing import Sequence

log_format = "%(asctime)s %(levelname)s %(processName)s %(threadName)s %(message)s"

logging.basicConfig(level=logging.INFO,
                    format=log_format,
                    datefmt="%Y%m%d %H:%M:%S")
logger = logging.getLogger(__name__)

RUBOCOP_DEFAULT_COMMAND = "--extra-details --display-style-guide --parallel"


def main(argv: Optional[Sequence[str]] = None) -> int:
    logger.debug("argv {}".format(argv))

    target_files = argv[1:]  # drop argv[0]
    logger.debug("target_files {}".format(target_files))

    path = pathlib.Path(target_files[0])
    project_path = str(pathlib.Path(*path.parts[0:2]))
    logger.debug("project_path {}".format(project_path))

    os.chdir(project_path)
    logger.debug("cwd {}".format(os.getcwd()))

    target_files = []
    for file_path in argv[1:]:
        file_path = file_path.replace(project_path + '/', '')
        if file_path in ["db/schema.rb"]:
            continue
        target_files.append(file_path)

    if len(target_files) == 0:
        return 0

    os.system("bundle install")

    cmd = "bundle exec rubocop {} {}".format(
        RUBOCOP_DEFAULT_COMMAND, ' '.join(target_files))
    logger.debug("cmd {}".format(cmd))

    ret = os.system(cmd)
    if ret != 0:
        ret = -1
    return ret


if __name__ == '__main__':
    exit(main(sys.argv))
