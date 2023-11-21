from collections import deque
from bokeh.transform import stack

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
    
    def reversed(self):
        return self.container.reverse()
    
if __name__ == "__main__":
    stack = Stack()
    stack.push('hajbdd')
    stack.reversed
    print(stack.reversed())

