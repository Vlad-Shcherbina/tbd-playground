import sys
import unittest

import nose
from nose.tools import eq_

from production.naive_misc import NaiveMisc
from production.cpp_misc.cpp_misc import CppMisc


def canonical_str(m):
    assert m.__class__.__name__.endswith('Misc')
    return str(m).replace(m.__class__.__name__, '*Misc')


class CommonMiscTests(object):

    Machine = None

    def test_minimal(self):
        m = self.Machine(2)
        m.set_word(0, 1)
        m.set_word(1, 0)
        m.set_word(2, 3)
        m.set_word(3, 2)
        eq_(canonical_str(m), '*Misc(ip=0, memory=[1, 0, 3, 2])')

        m.step()

        eq_(canonical_str(m), '*Misc(ip=0, memory=[1, 2, 3, 2])')


class NaiveMiscTests(unittest.TestCase, CommonMiscTests):
    Machine = NaiveMisc


class CppMiscTests(unittest.TestCase, CommonMiscTests):
    Machine = CppMisc


if __name__ == '__main__':
    nose.run_exit(argv=[
        sys.argv[0], __file__,
        '--verbose', '--with-doctest', '--logging-level=DEBUG'
    ])
