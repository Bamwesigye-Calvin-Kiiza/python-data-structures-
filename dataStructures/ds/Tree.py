class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level (self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent 
        return level
     
    def print_tree(self):
        spaces= ' '* self.get_level()*2
        prefix = spaces +'|__' if self.parent else ""
        print(prefix,self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
            
rootnode = TreeNode('Calvin Bamwesigye Kiiza')
level2 = TreeNode('highreach')
level2.add_child(TreeNode('Kamurasi Jordan'))
level2.add_child(TreeNode('Mukisa Jortham'))
level2.add_child(TreeNode('Ssozi Isaac'))

rootnode.add_child(level2)

rootnode.print_tree()