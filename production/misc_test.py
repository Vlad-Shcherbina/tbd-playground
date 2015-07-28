import sys

import nose
from nose.tools import eq_

from production.naive_misc import NaiveMisc


def test_minimal():
    m = NaiveMisc(word_size=2)
    m.set_word(0, 1)
    m.set_word(1, 0)
    m.set_word(2, 3)
    m.set_word(3, 2)
    eq_(str(m), 'NaiveMisc(ip=0, memory=[1, 0, 3, 2])')

    m.step()

    eq_(str(m), 'NaiveMisc(ip=0, memory=[1, 2, 3, 2])')


if __name__ == '__main__':
    nose.run_exit(argv=[
        sys.argv[0], __file__,
        '--verbose', '--with-doctest', '--logging-level=DEBUG'
    ])
