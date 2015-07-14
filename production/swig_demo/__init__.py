# Magically compile extension in this package when we try to import it.

import os
from distutils.core import setup, Extension

cur_dir = os.getcwd()
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    setup(
        name='sample',
        py_modules=['sample'],
        ext_modules=[
            Extension('_sample',
                ['sample.i', 'sample.cpp'],
                depends=['sample.h'],
                swig_opts=['-c++'],
            ),
        ],
        script_args=['build_ext', '--inplace']
    )
finally:
    os.chdir(cur_dir)
