class TreeNode:
    def __init__(self,data,designation):
        self.designation = designation
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
    
    def print_tree(self,display_type):
        if display_type == 'both':
            spaces = '  '* self.get_level()
            prefix = spaces + '|___'if self.parent else''
            print(prefix,self.data,'(',self.designation,')')
            if self.children:
                for child in self.children:
                    child.print_tree('both')
        elif display_type == 'designation':
            spaces = '  '* self.get_level()
            prefix = spaces + '|___'if self.parent else''
            print(prefix,self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree('designation')
        elif display_type == 'name':
            spaces = '  '* self.get_level()
            prefix = spaces + '|___'if self.parent else''
            print(prefix,self.data)
            if self.children:
                for child in self.children:
                    child.print_tree('name')
                
infra_head = TreeNode("Vishwa","Infrastructure Head")
infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
infra_head.add_child(TreeNode("Abhijit", "App Manager"))

cto = TreeNode("Chinmay", "CTO")
cto.add_child(infra_head)
cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
hr_head = TreeNode("Gels","HR Head")

hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

ceo = TreeNode("Nilupul", "CEO")
ceo.add_child(cto)
ceo.add_child(hr_head)


displaytype = input('Enter type of tree to display: ')
ceo.print_tree(display_type = displaytype)