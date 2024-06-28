class HashTable:
    # initialize the hash table with a size of 26 for the capital letters
    def __init__(self, size):
        self.size = size
        self.table = [-1] * size
    
    # hash function to get the index of the key
    def hash_function(self, key):
        return ord(key) - ord('A')
    
    # insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
    
    # search for a key in the hash table
    def search(self, key):
        index = self.hash_function(key)
        return self.table[index]

    def delete(self,key):
        index = self.hash_function(key)
        self.table[index] = -1