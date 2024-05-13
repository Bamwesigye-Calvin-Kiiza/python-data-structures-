from collections import deque
'''
Stack class to handle the stack operations in form of methods of OOP
'''

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, value):
        '''
        pushing or adding an element or object to the stack
        '''
        return self.container.append(value)
        
    def pop(self):
        '''
        removing an element or object on the top of the stack
        '''
        return self.container.pop()

    def peek(self):
        '''
        returning the most recently pushed element(item on the top)
        '''
        return self.container[-1]
        
    def isEmpty(self):
        '''
        checking if the stack is empty
        '''
        return len(self.container)==0 
    
    def length(self):
        '''
        returning the length of the stack
        '''
        return len(self.container) 
    
    def print_stack(self):
        '''
        print all elements in the stack
        '''
        lst = []
        for item in self.container: lst.append(item)
        return lst
    
    def reverse(self):
        '''
        reverse the stack data 
        '''
        strr = ''
        while self.length() != 0:
            strr += self.pop()
        return strr
    
if __name__ == '__main__':
    
    def form_stack(val):
        '''
        function to create the stack
        '''
        stack = Stack()
        for letter in val:
            stack.push(letter)
        stack.pop()
        print('Stack = ',stack.print_stack())
        print('Peek value: ',stack.peek())
        print('stack length = ',stack.length())
        print('Empty status: ',stack.isEmpty())
        print('reversed: ',stack.reverse())
        
    name = 'bamwesigye'  
    form_stack(name)