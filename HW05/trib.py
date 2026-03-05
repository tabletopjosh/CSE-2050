def trib(k):
    """
    Returns the kth tribonacci number using memoization.
    k=1 corresponds to T0=0, k=2 to T1=0, k=3 to T2=1.
    """
    return _trib(k, {})

def _trib(k, solved):
    """
    Recursive helper function with a memoization dictionary.
    """
    if k in solved:
        return solved[k]
    
    # Base cases for the 1st, 2nd, and 3rd terms
    if k == 1 or k == 2:
        return 0
    if k == 3:
        return 1
    
    # Recursive step
    solved[k] = _trib(k - 1, solved) + _trib(k - 2, solved) + _trib(k - 3, solved)
    return solved[k]