class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    # method to compute the hash value for a given key
    def _hash(self, key):
        return hash(key) % self.size
    # method to insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self._hash(key)
        # check if the key already exists in the table, if so, update the value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    # method to retrieve a value by key from the hash table
    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    # method to remove a key-value pair from the hash table
    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
# implementation of the hash table    
hash_table = HashTable()
hash_table.insert("name", "Sakirin")
hash_table.insert("major", "IT Engineering")
hash_table.insert("university", "RUPP")

print(hash_table.get("name"))
print(hash_table.get("major"))

hash_table.remove("major")

print(hash_table.get("major"))