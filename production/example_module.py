import os

from production import utils


def load_example():
    with open(os.path.join(utils.get_data_dir(), 'example.txt')) as fin:
        return fin.read()
