import sys
import unittest
import logging

logger = logging.getLogger(__name__)

import nose
from nose.tools import eq_
import hypothesis
import hypothesis.strategies as st
from hypothesis.testrunners.forking import ForkingTestCase

from production.naive_misc import NaiveMisc
from production.cpp_misc.cpp_misc import CppMisc
from production import testing_utils


def canonical_str(m):
    assert m.__class__.__name__.endswith('Misc')
    return str(m).replace(m.__class__.__name__, '*Misc')


class CommonMiscTests(object):

    Machine = None

    # Unnecessary for NaiveMisc, but decorating CppMisc tests conditionally
    # is messy.
    @testing_utils.isolate_process_failures()
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


class MiscEquivalenceTests(unittest.TestCase):

    def execute_example(self, f):
        return testing_utils.isolating_executor(f)

    @hypothesis.given(
        st.integers(2, 8),
        st.streaming(st.integers(0, 2**8)),
        st.integers(min_value=0, max_value=100))
    def misc_equivalence_test(self, word_size, memory, num_steps):
        m1 = NaiveMisc(word_size)
        for i in range(2**word_size):
            m1.set_word(i, memory[i] % 2**word_size)

        m2 = CppMisc(word_size)
        for i in range(2**word_size):
            m2.set_word(i, memory[i] % 2**word_size)

        logger.info('start configuration: {}'.format(canonical_str(m1)))
        eq_(canonical_str(m1), canonical_str(m2))

        logger.info('simulating {} steps'.format(num_steps))
        m1.simulate(num_steps)
        m2.simulate(num_steps)

        eq_(canonical_str(m1), canonical_str(m2))


if __name__ == '__main__':
    nose.run_exit(argv=[
        sys.argv[0], __file__,
        '--verbose', '--with-doctest', '--logging-level=DEBUG'
    ])
