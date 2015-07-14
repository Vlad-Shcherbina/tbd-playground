import sys, os

import nose

from production import utils


if __name__ == '__main__':
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',

        # Othersie it fails, probably because of some weird interaction between
        # distutils argv and nose argv.
        '--exclude-dir=' + os.path.join(
            utils.get_project_root(), 'production', 'swig_demo'),
        ]
    nose.run_exit(argv=argv)
