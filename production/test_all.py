import sys, os

import nose


if __name__ == '__main__':
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        '--exclude-dir=swig_demo',
        ]
    nose.run_exit(argv=argv)
