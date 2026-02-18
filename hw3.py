import random
import time

def generate_lists(size):
    """Generates two lists of unique random integers of a given size."""
    list1 = random.sample(range(0, size * 2), size)
    list2 = random.sample(range(0, size * 2), size)
    return list1, list2

def find_common(list1, list2):
    """Finds the number of common items between two lists using a nested loop."""
    # Analysis:
    count = 0                  # 1 operation
    for item1 in list1:        # n iterations
        for item2 in list2:    # n iterations per item1
            if item1 == item2: # 1 operation
                count += 1     # 1 operation
    return count               # 1 operation
    # Time Complexity: O(n^2)

def find_common_efficient(list1, list2):
    """Finds the number of common items between two lists using a set."""
    # Analysis:
    set1 = set(list1)          # n operations
    count = 0                  # 1 operation
    for item2 in list2:        # n iterations
        if item2 in set1:      # 1 operation
            count += 1         # 1 operation
    return count               # 1 operation
    # Time Complexity: O(n)

def measure_time():
    """Measures and prints the execution time of the functions."""
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    
    print(" List Size   find_common Time (s)   find_common_efficient Time (s)")
    print("-----------  ----------------------   ------------------------------")
    
    for size in sizes:
        l1, l2 = generate_lists(size)
        
        start1 = time.time()
        find_common(l1, l2)
        end1 = time.time()
        time1 = f"{end1 - start1:.6f}"
        
        start2 = time.time()
        find_common_efficient(l1, l2)
        end2 = time.time()
        time2 = f"{end2 - start2:.6f}"
        
        print(f"{size:>10}   {time1:>22}   {time2:>30}")

if __name__ == "__main__":
    measure_time()