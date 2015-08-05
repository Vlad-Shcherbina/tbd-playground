A place to figure out and standardize trivial technical details like project
layout, how to run tests, what should be in the environment, etc. So that we
don't waste time on it during the contest.


## Setup, environment, dependencies

We use quite a variety of OSs, IDEs, and other tools, so there is no attempt to fully standardize the environment or setup instructions. Here are some approximate recommendations, and let's hope that differences in minor version numbers or subtle quirks like that will not bite us in the least expected moment. If somebody volunteers to write more detailed instructions for a particular OS - you are welcome.

CPython 3.4.3 (latest stable release).

Virtualenv is optional.

Third-party python libraries:
 - pip install nose
 - pip install coverage
 - TODO

Root of this repository should be in `PYTHONPATH`, because imports of our modules are absolute (`from production import utils`). There are several ways to achieve that:
  - add project path to the environment variable (before the contest, don't forget to change path from `tbd-playground` to the actual repository; same for other methods)
  - add file `<python installation or venv>/lib/python3.4/site-packages/tbd.pth` whose content is a single line with project path
  - configure your favorite IDE appropriately
  - run scripts as `python3 -m production.some_script` instead of `python3 production/some_script.py`, then the location of package `production` will be automatically added to `PYTHONPATH`.

In the code, don't rely on current directory to fetch assets. There will be something like `utils.get_data_dir()`.

To avoid forgetting running tests before push, consider setting up git hook
(see `git_hooks/`).
