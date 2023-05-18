class MyHashTable:
    def __init__(self, size):
        self.data = [list() for _ in range(size)]

    def _hash(self, key):
        hash_number = 0
        for i in range(len(key)):
            hash_number = (hash_number + ord(key[i]) * i) % len(self.data)
        return hash_number

    def set(self, key, value):
        index = self._hash(key)
        if not self.data[index]:
            self.data[index].append([key, value])
        else:
            self.data[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        if self.data[index]:
            for k, v in self.data[index]:
                if k == key:
                    return v
        return None


my_hash = MyHashTable(10)
my_hash.set('grapes', 10000)
my_hash.set('apples', 538)
print(my_hash.get('grapes'))
print(my_hash.get('apples'))
