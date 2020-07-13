#!/usr/bin/env python3

import os
import glob

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

def main():
    config_glob_pattern = "{root_dir}{path_sep}*{path_sep}{pre_commit_config}".format(
        root_dir = ROOT_DIR,
        path_sep = os.path.sep,
        pre_commit_config = ".pre-commit-config.yaml"
    )

    for config_file in glob.glob(config_glob_pattern):
        cmd = "pre-commit run --verbose --config {}".format(config_file)
        print("\nExecuting - {}\n\n".format(cmd))
        ret = os.system(cmd)
        if ret != 0:
            return ret
    return 0

if __name__ == '__main__':
    exit(main())
