def solve_puzzle(L):
    """Returns True if a given board is solveable, False otherwise."""
    return _solve_puzzle(L, 0, set())

def _solve_puzzle(L, idx, visited):
    """Helper function to recursively solve the puzzle with memoization."""
    # Base case: reached the final tile
    if idx == len(L) - 1:
        return True
        
    # Base case: already visited this tile (avoid infinite loops)
    if idx in visited:
        return False
        
    visited.add(idx)
    
    # Calculate next possible moves using modulo to wrap around
    idx_cw = (idx + L[idx]) % len(L)
    idx_ccw = (idx - L[idx]) % len(L)
    
    # Recursively check both paths
    return _solve_puzzle(L, idx_cw, visited) or _solve_puzzle(L, idx_ccw, visited)