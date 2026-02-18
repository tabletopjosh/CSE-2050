import random
import time

def generate_lists(size):
    """
    Generates two lists of unique random integers of a given size.
    """
    list1 = random.sample(range(0, size * 2), size)
    list2 = random.sample(range(0, size * 2), size)
    return list1, list2

def find_common(list1, list2):
    """
    Finds the number of common items between two lists using a nested loop.
    No high-level collections used for the search logic.
    """
    # Analysis:
    count = 0                  # 1 operation
    for item1 in list1:        # n iterations
        for item2 in list2:    # n iterations per item1
            if item1 == item2: # 1 operation (comparison)
                count += 1     # 1 operation (increment)
    return count               # 1 operation
    # Time Complexity: O(n^2) - Quadratic

def find_common_efficient(list1, list2):
    """
    Finds the number of common items between two lists using a set for O(1) lookups.
    """
    # Analysis:
    set1 = set(list1)          # n operations (to hash all elements into a set)
    count = 0                  # 1 operation
    for item2 in list2:        # n iterations
        if item2 in set1:      # 1 operation (O(1) average case for set lookup)
            count += 1         # 1 operation
    return count               # 1 operation
    # Time Complexity: O(n) - Linear

def measure_time():
    """
    Measures and prints the execution time of find_common and find_common_efficient
    for various input sizes in a formatted table.
    """
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    
    print(f"{'List Size':>10}   {'find_common Time (s)':>22}