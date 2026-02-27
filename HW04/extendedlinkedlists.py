from linkedlist import Node, LinkedList # get linkedlist.py from lab

class ReversableLinkedList(LinkedList):
    """A linked list that can be reversed in place."""
    
    def reverse(self) -> None:
        """Reverses the linked list by redirecting node links without creating new nodes."""
        prev = None
        current = self._head
        self._tail = self._head
        
        while current is not None:
            next_node = current.link
            current.link = prev
            prev = current
            current = next_node
            
        self._head = prev


class SortedLinkedList(LinkedList):
    """A linked list that maintains its items in sorted order."""
    
    def add_first(self, item):
        """Disabled to maintain sorted order."""
        raise NotImplementedError(f"Use add_sorted({item}) instead")
        
    def add_last(self, item):
        """Disabled to maintain sorted order."""
        raise NotImplementedError(f"Use add_sorted({item}) instead")
        
    def add_sorted(self, item) -> None:
        """Inserts an item into the linked list in sorted order."""
        new_node = Node(item)
        
        # Empty list
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._len += 1
            return
            
        # Insert at the beginning
        if item <= self._head.item:
            new_node.link = self._head
            self._head = new_node
            self._len += 1
            return
            
        # Iterate to find the correct insertion point
        prev = None
        curr = self._head
        while curr is not None and curr.item < item:
            prev = curr
            curr = curr.link
            
        # Insert the node
        prev.link = new_node
        new_node.link = curr
        
        # Update tail if inserted at the end
        if curr is None:
            self._tail = new_node
            
        self._len += 1


class UniqueLinkedList(LinkedList):
    """A linked list that can remove duplicate items."""
    
    def remove_dups(self) -> dict:
        """Removes duplicate items, keeping the first occurrence, and returns a dict of removed counts."""
        removed_counts = {}
        
        if self._head is None:
            return removed_counts
            
        # Initialize dictionary with 0s for all items
        curr = self._head
        while curr is not None:
            if curr.item not in removed_counts:
                removed_counts[curr.item] = 0
            curr = curr.link
            
        seen = set([self._head.item])
        prev = self._head
        curr = self._head.link
        
        # Iterate and remove duplicates
        while curr is not None:
            if curr.item in seen:
                removed_counts[curr.item] += 1
                prev.link = curr.link
                self._len -= 1
                if curr == self._tail:
                    self._tail = prev
            else:
                seen.add(curr.item)
                prev = curr
            curr = curr.link
            
        return removed_counts