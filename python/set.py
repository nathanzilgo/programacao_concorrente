
class Set:
    def __init__(self, size=10):
        self._size = size
        # # initialize hashing function
        # self._hash_function = lambda x: hash(x) % self._size
        # current amount of the elements in array
        self._filled = 0
        # initialize and prepopulate list of length size given in constructor
        self._element = [[] for _ in range(size)]

    def _hash_function(self, value):
        return hash(value) % self._size

    def _contains(self, value):
        for i, e in enumerate(self._element[self._hash_function(value)]):
            if value == e:
                return i
        return -1

    def contains(self, value):
        return self._contains(value) >= 0

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def __iter__(element):
        pass
