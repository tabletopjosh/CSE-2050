class Entry:
    def __init__(self, item, priority):
        # Gives entries an item and a priority [cite: 7]
        self.item = item
        self.priority = priority

    def __lt__(self, other):
        # Returns True if self has a lower priority than other [cite: 8]
        return self.priority < other.priority

    def __eq__(self, other):
        # Returns True if the two entries have the same priority and item [cite: 8]
        return self.priority == other.priority and self.item == other.item

class PQ_UL:
    def __init__(self):
        self._entries = []

    def __len__(self):
        # Returns the number of entries in the priority queue [cite: 13]
        return len(self._entries)

    def insert(self, item, priority):
        # Adds item with given priority to priority queue [cite: 16]
        self._entries.append(Entry(item, priority))

    def find_min(self):
        # Returns (but does not remove) the object with minimum priority [cite: 18]
        if not self._entries:
            return None
        return min(self._entries) 

    def remove_min(self):
        # Removes and returns the object with minimum priority [cite: 21]
        if not self._entries:
            return None
        min_entry = self.find_min()
        self._entries.remove(min_entry)
        return min_entry

class PQ_OL:
    def __init__(self):
        self._entries = []

    def __len__(self):
        # Returns the number of entries in the priority queue [cite: 13]
        return len(self._entries)

    def insert(self, item, priority):
        # Adds item with given priority to priority queue [cite: 16]
        self._entries.append(Entry(item, priority))
        # Keep it sorted
        self._entries.sort() 

    def find_min(self):
        # Returns (but does not remove) the object with minimum priority [cite: 18]
        if not self._entries:
            return None
        return self._entries[0]

    def remove_min(self):
        # Removes and returns the object with minimum priority [cite: 21]
        if not self._entries:
            return None
        return self._entries.pop(0)