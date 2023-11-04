class Binarysearchtreenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if data == self.data:
            ...
        if data < self.data:
            if self.left:
                return self.left.add_child(data)
            else:
                self.left =  Binarysearchtreenode(data)
            
        if data > self.data:
            if self.right:
                return self.right.add_child(data)
            else:
                self.right = Binarysearchtreenode(data)
                
    def in_order_traversal(self):
        elements = []
        
        # visit left 
        if self.left:
            elements += self.left.in_order_traversal()
        # visit root node
        elements.append(self.data)
        
        # vist right
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def search(self,val):
        if self.data == val:
            return True
        
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
    def find_max(self):
        max = self.data
        if self.right:
            return self.right.find_max()
        else: return max
        
    def find_min(self):
        min = self.data
        if self.left:
            return self.left.find_min()
        else: return f'min is {min}'
        
    def find_sum(self):
        sum = self.data
        
        if self.left:
            sum += self.left.find_sum()
        
        if self.right:
            sum += self.right.find_sum() 
        
        return sum 
    def delete(self,value):
        if value<self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.left
            if self.right is None:
                return self.left
            
            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete(max_value)
            
        return self
    
        
        
def buildtree(elements):
    root = Binarysearchtreenode(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])
        
    return root

random_list = [80,15,30,81,101,3,5,22,6,7,9,1]
number = 101
numbers_tree = buildtree(random_list)
print(numbers_tree.in_order_traversal())
print(numbers_tree.search(100))
print(numbers_tree.find_max())
print(numbers_tree.find_min())
print(numbers_tree.find_sum())
# print(numbers_tree.delete(number))
numbers_tree.delete(number)
print('after deleting ',number,': ',numbers_tree.in_order_traversal())
 