class Node:
    """Recursively implements Linked List functionality"""
    def __init__(self, data, link=None):
        """Instantiates a new Node with given data"""
        self.data = data
        self.link = link

    def __repr__(self):
        """Returns string representation of node"""
        return f"Node({self.data})"
    
    def __len__(self):
        """Recursively calculates length of sublist starting at this node"""
        if self.link is None:
            return 1
        return 1 + len(self.link)

    def get_tail(self):
        """Recursively finds the data stored in the tail of this sublist"""
        if self.link is None:
            return self.data
        return self.link.get_tail()
    
    def add_last(self, data):
        """Recursively adds to end of this sublist"""
        if self.link is None:
            self.link = Node(data)
        else:
            self.link.add_last(data)

    def total(self):
        """Recursively adds all items"""
        if self.link is None:
            return self.data
        return self.data + self.link.total()
    
    def remove_last(self):
        """
        Recursively removes last item in sublist.
        Returns a tuple of (new_head, tail_data).
        """
        # Base case: this node is the tail
        if self.link is None:
            return None, self.data
        
        # Recursive case: update link with what the next node returns
        new_node_link, tail_data = self.link.remove_last()
        self.link = new_node_link
        return self, tail_data

    def reverse(self, prev):
        """
        Recursively reverse list.
        Redirects links and returns the new head of the list.
        """
        original_next = self.link
        self.link = prev
        
        # Base case: we reached the original tail
        if original_next is None:
            return self
        
        # Recursive case: pass back the new head
        return original_next.reverse(self)