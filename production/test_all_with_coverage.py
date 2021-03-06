import sys, os

import nose
import coverage.cmdline

from production import testing_utils


if __name__ == '__main__':
    testing_utils.make_hypothesis_reproducible()
    testing_utils.disable_isolation()

    argv = sys.argv + [
        'production',
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        '--with-coverage', '--cover-branches', '--cover-erase',
        '--cover-package=production',
        ]
    nose.main(argv=argv, exit=False)

    cur_dir = os.getcwd()
    try:
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        coverage.cmdline.main(argv=['html'])
    finally:
        os.chdir(cur_dir)
