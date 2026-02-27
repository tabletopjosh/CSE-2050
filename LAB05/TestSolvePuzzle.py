from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
    def testClockwise(self):
        """Tests a board solveable using only CW moves"""
        # Moves: 0 -> 1 -> 2 -> 3 (goal)
        self.assertTrue(puzzle([1, 1, 1, 0]))

    def testCounterClockwise(self):
        """Tests a board solveable using only CCW moves"""
        # Moves: 0 -> 2 -> 4 (goal)
        self.assertTrue(puzzle([3, 0, 3, 0, 0]))

    def testMixed(self):
        """Tests a board solveable using only a combination of CW and CCW moves"""
        # Example from the assignment instructions
        self.assertTrue(puzzle([3, 6, 4, 1, 3, 4, 2, 0]))
        
    def testUnsolveable(self):
        """Tests an unsolveable board"""
        # Example from the assignment instructions
        self.assertFalse(puzzle([3, 4, 1, 2, 0]))

if __name__ == '__main__':
    unittest.main()