

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str) -> int:
        return sum(ord(c) for c in string)
    
    def add(self, key, value):
        key_hash = self.hash(key)
        if key_hash not in self.collection.keys():
            self.collection[key_hash] = {}
        self.collection[key_hash][key] = value
    
    def remove(self, key):
        key_hash = self.hash(key)
        if key_hash not in self.collection.keys():
            return
        if key not in self.collection[key_hash].keys():
            return
        del self.collection[key_hash][key]
    
    def lookup(self, key):
        key_hash = self.hash(key)
        if key_hash not in self.collection.keys():
            return None
        if key not in self.collection[key_hash].keys():
            return None
        return self.collection[key_hash][key]


hash_table = HashTable()
print(hash_table.hash('golf'))
hash_table.add('golf', 'sport')
hash_table.add('soccer', 'sport')
hash_table.add('fcc', 'coding')
hash_table.add('cfc', 'chemical')
hash_table.remove('cfc')
hash_table.remove('fcc')
hash_table.remove('cfc')
print(hash_table.lookup('cfc'))
print(hash_table.lookup('soccer'))

print(hash_table.collection)
