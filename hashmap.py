import threading


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 150
        self.map = [None] * self.capacity

    def hash(self, key):
        hash = 0
        for char in key:
            hash = ord(char) + hash * 37
        return hash % self.capacity

    def put(self, key, value):
        hash = self.hash(key)
        lock = threading.Lock()
        lock.acquire()
        print(f'Hash: {hash}')
        if self.map[hash] is None:
            self.map[hash] = [key, value]
            self.size += 1
        else:
            self.map[hash][1] = value
            self.size += 1
        lock.release()

    def get(self, key):
        hash = self.hash(key)
        if self.map[hash] is None:
            return None
        else:
            return self.map[hash][1]

    def print(self):
        print(list(filter(lambda x: x is not None, self.map)))


hm = HashMap()
hm.put('abc', 55)
hm.put('bca', 42)
hm.put('acb', 235898)
hm.put('ccc', 5388 ** 2)
print(hm)
hm.print()
