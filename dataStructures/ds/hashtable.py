#take note that hashtable is a dictionary implementation in python

class Hashtable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]
        
    def get_hash(self, key):
        h = 0 
        for element  in key:
                h += ord(element)      
        return h%self.Max
        
    def __setitem__ (self, key, val):
        h = self.get_hash(key)
        
        found = False
        for i, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][i] = (key,val)
                found = True
                break 
        if not found:   
            self.arr[h].append((key,val))
            
    def __getitem__(self,key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self,key):
        h = self.get_hash(key)
        for i, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][i]
        
if __name__ == '__main__':
    x = Hashtable()
    x['age'] = 63
    x['age']
    print(x.arr)
            