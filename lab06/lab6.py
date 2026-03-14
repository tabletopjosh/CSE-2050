class OrderedList:
    def __init__(self, items=None):
        """Initialize an ordered list. If `items` is specified, the OrderedList starts with the items in that collection"""
        self._L = sorted(list(items)) if items is not None else list()
            
    def add(self, item):
        """adds item to the list and maintains sorted order"""
        self._L.append(item)
        self._L.sort()

    def remove(self, item):
        """removes the first occurrence of item from the list. Raise a RuntimeError if the item is not present."""
        if not item in self: 
            raise RuntimeError(f"{item} not in OrderedList")
        self._L.remove(item)

    def __getitem__(self, index):
        """returns the item with the given index in the sorted list. This is also known as selection."""
        return self._L[index]

    def __iter__(self):
        """returns an iterator over the ordered list that yields the items in sorted order. Required for `for` loops."""
        return iter(self._L)

    def __len__(self):
        """returns the length of the ordered list."""
        return len(self._L)

    def __contains__(self, item):
        """returns true if there is an element in the list equal to item using binary search."""
        return self._bs(item, 0, len(self._L) - 1)

    def _contains_list(self, item):
        """returns True iff there is an item of the list equal to item."""
        return item in self._L 

    def _contains_bs_slow(self, item):
        """wrapper for the slow slicing-based binary search"""
        return self.__contains_bs_slow(self._L[:], item)
    
    def __contains_bs_slow(self, L, item):
        """searches L for item. This is slow since it slices L at every level of recursion"""
        if len(L) == 0: return False            
        median = len(L) // 2
        if item == L[median]: return True
        elif item < L[median]: return self.__contains_bs_slow(L[:median], item)
        else: return self.__contains_bs_slow(L[median + 1:], item)

    def _bs(self, item, left, right):
        """
        searches for item using `left` and `right` indices instead of slicing.
        Running time: O(log n)
        """
        # Base case: search range is empty
        if left > right:
            return False

        mid = (left + right) // 2

        # Base case: found item
        if self._L[mid] == item:
            return True
        
        # Recursive step: item is in smaller half
        elif item < self._L[mid]:
            return self._bs(item, left, mid - 1)
        
        # Recursive step: item is in bigger half
        else:
            return self._bs(item, mid + 1, right)