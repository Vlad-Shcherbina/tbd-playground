import sys, os

import nose


if __name__ == '__main__':
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        ]
    nose.run_exit(argv=argv)
