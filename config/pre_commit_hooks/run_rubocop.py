#!/usr/bin/env python3

import os
import sys

from typing import Optional
from typing import Sequence

cwd = os.getcwd()

def main(argv: Optional[Sequence[str]] = None) -> int:
    argv = argv[1:]
    print("argv {}".format(argv))
    project_dir = '/'.join(argv[-1].split('/')[0:2])
    os.chdir(project_dir)

    print("cwd {}".format(os.getcwd()))

    target_files = []
    for f in argv:
        if '.pre-commit-config.yaml' in f:
            continue
        target_files.append('/'.join(f.split('/')[2:]))

    cmd = "rubocop {}".format(' '.join(target_files))

    print("cmd {}".format(cmd))

    return os.system(cmd)
    # return 0

if __name__ == '__main__':
    ret = -1
    try:
        ret = main(sys.argv)
    finally:
        os.chdir(cwd)
        print("cwd {} - {}".format(os.getcwd(), ret))

    if ret != 0:
        exit(-1)
    else:
        exit(0)
