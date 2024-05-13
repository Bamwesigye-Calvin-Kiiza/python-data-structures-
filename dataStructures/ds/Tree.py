class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent 
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        print(' '*self.get_level()*2,"|--" if self.parent else '',self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


rootnode = TreeNode('Electronics')
laptops = TreeNode('Laptops')
phones = TreeNode('phones')
acer = TreeNode('acer')
macbook = TreeNode('Macbook')
HP = TreeNode('HP')
sumsung = TreeNode('sumsung')
iphone = TreeNode('Iphone')
rootnode.add_child(laptops)
rootnode.add_child(phones)
laptops.add_child(acer)
laptops.add_child(macbook)
phones.add_child(iphone)
phones.add_child(sumsung)
rootnode.print_tree()