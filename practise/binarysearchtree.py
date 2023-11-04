class Binarysearchtreenode:
    def __init__(self,node_data):
        self.node_data = node_data
        self.left_node = None
        self.right_node = None
        
    def add_node(self,node_data):
        if self.node_data == node_data:
            pass 
        if node_data < self.node_data:
            if self.left_node:
                return self.left_node.add_node(node_data)
            else: self.left_node = Binarysearchtreenode(node_data)
            
        if node_data > self.node_data:
            if self.right_node:
                return self.right_node.add_node(node_data)
            else:self.right_node = Binarysearchtreenode(node_data)
    
    def find_sum(self):
        sum = self.node_data
        if self.left_node:
            sum += self.left_node.find_sum()
        
        if self.right_node:
            sum += self.right_node.find_sum()
        return sum

    def find_min (self):
        min = self.node_data
        if self.left_node:
            min = self.left_node.find_min()
        return min
    def find_max (self):
        max = self.node_data
        if self.right_node:
            max = self.right_node.find_max()
        return max
    def search(self,value):
        if self.node_data == value:
            return True
        if value < self.node_data:
            if self.left_node:
                return self.left_node.search(value)
            else: return False
        if value > self.node_data:
            if self.right_node:
                return self.right_node.search(value)
            else:return False
            
    def in_order_traversal(self):
        elements = []
        # visit the left 
        if self.left_node:
            elements += self.left_node.in_order_traversal()
        # add the root node 
        elements.append(self.node_data)
        
        # visit the right 
        if self.right_node:
            elements += self.right_node.in_order_traversal()
        
        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        # visit root node
        elements.append(self.node_data)
        
        if self.left_node:
            elements += self.left_node.pre_order_traversal()
        if self.right_node:
            elements += self.right_node.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left_node :
            elements += self.left_node.post_order_traversal()
        if self.right_node:
            elements += self.right_node.pre_order_traversal()
        elements.append(self.node_data)
        return elements
        
def buildTree(array):
    tree = Binarysearchtreenode(array[0]) 
    for i in range(1, len(array)):
        tree.add_node(array[i])
    return tree

number = 101
array = [15,12,27,20,88,23,14,7]
binarytree = buildTree(array)
print('Sum of elememnts: ',binarytree.find_sum())
print('Min number in list: ',binarytree.find_min())
print('Max number in list: ',binarytree.find_max())
print('Existance of ',number,'in list is: ',binarytree.search(number))
print('In_order_traversed list: ',binarytree.in_order_traversal())
print('Pre_order_traversed list: ',binarytree.pre_order_traversal())
print('Post_order_traversed list: ',binarytree.post_order_traversal())