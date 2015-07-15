import sys, os

import nose
import coverage.cmdline


if __name__ == '__main__':

    cur_dir = os.getcwd()
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        argv = sys.argv + [
            '--verbose', '--with-doctest',
            '--logging-level=DEBUG',
            '--with-coverage', '--cover-branches', '--cover-erase',
            '--cover-package=production',
            ]
        nose.main(argv=argv, exit=False)

        coverage.cmdline.main(argv=['html'])

    finally:
        os.chdir(cur_dir)
