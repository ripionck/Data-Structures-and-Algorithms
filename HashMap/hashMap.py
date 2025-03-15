class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def hash_function(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
        
    # Allow multiples value for the same key
    #def put(self, key, value):
        #index = self.hash_function(key)
        #for pair in self.table[index]:
            #if pair[0] == key:
                #pair[1].append(value)  # Append the new value to the list
                #return
        #self.table[index].append([key, [value]])  # Initialize a list for values
        
    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
            
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
            
            
hash_map = HashMap()

hash_map.put('name', 'Alice')
hash_map.put('name', 'John')
#hash_map.put('age', 30)
#hash_map.put('city', 'New York')

hash_map.get('name')
hash_map.get('age')

hash_map.remove('name')
