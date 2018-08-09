import unittest
from forever_young import *


class MyTestCase(unittest.TestCase):

    def testACM1(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(32, 20), 16)

    def testACM2(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(2016, 100), 42)

    def testACM3(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(55, 35), 16)

    def testCustom1(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(417, 200), 13)

    def testCustom2(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(2031, 363), 25)

    def testStress(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(65348348552974, 125), 11)


if __name__ == '__main__':
    unittest.main()
