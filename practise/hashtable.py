class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [[]for i in range(self.Max)]
        
    def get_hash(self,key):
        h = 0
        for character in key:
            h += ord(character)
        return h%self.Max
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        
        found = False
        for i , element in enumerate(self.arr[h]):
            if element[1] == key:
                self.arr[h][i] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    def __delitem__(self,key):
        h = self.get_hash(key)
        for i,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i]

if __name__ == '__main__':
    x = HashTable()
    x['age'] = 63
    x['age']
    print(x.arr)               