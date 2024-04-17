import sys
import time

import unittest

class PipeTestCases(unittest.TestCase):
    def test_basic(self):
        self.assertEqual([1,2,3] |> sum(), 6)
        self.assertEqual(range(5) |> map(str) |> ', '.join(), '0, 1, 2, 3, 4')

if __name__ == "__main__":
    unittest.main()
