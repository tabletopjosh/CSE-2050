import unittest
from trib import trib

class TestTrib(unittest.TestCase):
    def test_first_ten(self):
        """Tests the first 10 numbers in the tribonacci series"""
        # Mapping rank k to the expected value (T_0 through T_9)
        solutions = {
            1: 0, 2: 0, 3: 1, 4: 1, 5: 2, 
            6: 4, 7: 7, 8: 13, 9: 24, 10: 44
        }
        for k in solutions:
            self.assertEqual(trib(k), solutions[k], f"Failed at k={k}")

    def test_one_hundred(self):
        """Ensures trib(100) returns the 100th term (T_99)"""
        expected = 28992087708416717612934417
        self.assertEqual(trib(100), expected)

if __name__ == '__main__':
    unittest.main()