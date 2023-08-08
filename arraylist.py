
class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.map = [None] * self.capacity

    def hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.capacity
