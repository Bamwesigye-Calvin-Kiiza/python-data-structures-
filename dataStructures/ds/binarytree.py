class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
    def add_child(self,data):
        if self.data == data:
            return ...
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)          
                
    def in_oder_traversal(self):
        elements = []
    # visit left wing first  
        if self.left:
            elements += self.left.in_oder_traversal()
        
    # visit the root node now
        elements.append(self.data)
        
    # visit right wing
        if self.right:
            elements += self.right.in_oder_traversal()
            
        return elements
    
    def search(self,val):
        if self.data == val: return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else: 
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
             
def build_tree(arr):
    root = BinarySearchTree(arr[0])
    
    for i in range(1,len(arr)):
        root.add_child(arr[i])    
        
    return root
    
if __name__ == "__main__":
    numbers = [10, 20, 33, 24, 50, 6, 7]
    
    print(build_tree(numbers).search(7))
    
    
