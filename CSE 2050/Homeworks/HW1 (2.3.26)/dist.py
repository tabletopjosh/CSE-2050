
def dist(n):
    """
    Returns True if all integers in the list n are distinct (unique).
    """
    # A set only keeps unique items. If the size matches the original list, 
    # then no duplicates were removed, meaning all numbers were distinct.
    return len(n) == len(set(n))