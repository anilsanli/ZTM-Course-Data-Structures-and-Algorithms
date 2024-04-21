class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append((key, value))
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for pair in current_bucket:
                if pair[0] == key:
                    return pair[1]
        return None

my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000)
print(my_hash_table.get('grapes'))
my_hash_table.set('apples', 9)
print(my_hash_table.get('apples'))
