#!/usr/bin/env python

import json
import logging
import os
import re
import sys

from typing import Optional
from typing import Sequence

logger = logging.getLogger(__name__)


def main(argv: Optional[Sequence[str]] = None) -> int:

    logger.warning("argv {}".format(argv))

    try:
        with open("/tmp/files.json") as f:
            files = json.load(f)
    except Exception as e:
        logger.exception("Exception occured")
        return -1

    if len(argv) == 1:
        path_regex = re.compile("^(?:(?!src).)")
    else:
        path_regex = re.compile(argv[1])

    logger.warning("path_regx {}".format(path_regex))

    filenames = []

    for file in files:
        filename = file["filename"]
        if path_regex.match(filename):
            filenames.append(filename)

    logger.warning("filenames {}".format(filenames))

    cmd = "pre-commit run --verbose --files {}".format(
        ' '.join(filenames))
    logger.warning("cmd {}".format(cmd))

    ret = os.system(cmd)
    if ret != 0:
        ret = -1
    return ret


if __name__ == "__main__":
    exit(main(sys.argv))
