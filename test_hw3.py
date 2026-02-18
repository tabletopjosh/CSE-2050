import unittest
from hw3 import generate_lists, find_common, find_common_efficient

class TestHW3(unittest.TestCase):
    """
    Unit tests to verify the correctness of the functions in hw3.py.
    """
    
    def test_generate_lists(self):
        """Tests if generate_lists returns unique elements and correct lengths."""
        size = 50
        l1, l2 = generate_lists(size)
        self.assertEqual(len(l1), size)
        self.assertEqual(len(l2), size)
        self.assertEqual(len(set(l1)), size, "List 1 elements are not unique")
        self.assertEqual(len(set(l2)), size, "List 2 elements are not unique")

    def test_find_common(self):
        """Tests the nested loop common item finder."""
        l1 = [1, 2, 3, 4, 5]
        l2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_common(l1, l2), 2)
        self.assertEqual(find_common([10, 20], [30, 40]), 0)

    def test_find_common_efficient(self):
        """Tests the set-based common item finder."""
        l1 = [1, 2, 3, 4, 5]
        l2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_common_efficient(l1, l2), 2)
        self.assertEqual(find_common_efficient([10, 20], [30, 40]), 0)

if __name__ == "__main__":
    unittest.main()