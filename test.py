import unittest
from forever_young import *


class MyTestCase(unittest.TestCase):
    def test(self):
        solver = Solver()

        self.assertEqual(solver.forever_young(32, 20), 16)
        self.assertEqual(solver.forever_young(2016, 100), 42)
        self.assertEqual(solver.forever_young(55, 35), 16)
        self.assertEqual(solver.forever_young(417, 200), 13)
        self.assertEqual(solver.forever_young(2031, 363), 25)
        #self.assertEqual(solver.forever_young(65348348552974, 125), 11)


if __name__ == '__main__':
    unittest.main()
