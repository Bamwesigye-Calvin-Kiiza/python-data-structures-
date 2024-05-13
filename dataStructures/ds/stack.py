from collections import deque
# from bokeh.transform import stack

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
        
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    
    
if __name__ == "__main__":
    def reverse(data):
        stack = Stack()
        for later in data:
            stack.push(later)
        
        strr = ''
        
        while stack.size()!=0:
            strr += stack.pop()
         
        return strr    
     
    print(reverse('Calvin'))