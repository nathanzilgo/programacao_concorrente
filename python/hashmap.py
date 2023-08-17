import threading


class HashMap:
    def __init__(self, size=0, capacity=150):
        self.size = size
        self.capacity = capacity
        self.bucket = [None] * self.capacity
        self.locks = [threading.Lock() for _ in range(self.capacity)]  # Um lock por bucket

    def hash(self, key):
        hash = 0
        for char in key:
            hash = ord(char) + hash * 37
        return hash % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        with self.locks[index]:
            if self.bucket_array[index] is None:
                self.bucket_array[index] = []
            self.bucket_array[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        with self.locks[index]:
            if self.bucket_array[index] is not None:
                for stored_key, value in self.bucket_array[index]:
                    if stored_key == key:
                        return value
        return None

    def remove(self, key):
        index = self._hash(key)
        with self.locks[index]:
            if self.bucket_array[index] is not None:
                for i, (stored_key, _) in enumerate(self.bucket_array[index]):
                    if stored_key == key:
                        self.bucket_array[index].pop(i)
                        return
        raise KeyError(f"Key '{key}' not found.")

    def print(self):
        print(list(filter(lambda x: x is not None, self.bucket)))


hm = HashMap()
hm.put('abc', 55)
hm.put('bca', 42)
hm.put('acb', 235898)
hm.put('ccc', 5388 ** 2)
print(hm)
hm.print()
