class Node:
    def __init__(self,value = None ,next= None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def top_push(self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print_list(self):
        if self.head is None:
            return Exception("No element in list")

        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.value) + '->'
            itr = itr.next
        print(llstr)
        
    def  bottom_push(self,data):
        if self.head is None:
            node = Node(data,None)
            self.head = node
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)
        
    def list_length(self):
        itr = self.head
        count = 0 
        
        while itr:
            itr = itr.next
            count += 1
            
        return count
    
    def insert_at_index(self,data,index):
        if index == 0:
            self.head = Node(data,self.head)
            
        if index < 0 or index >= self.list_length():
            return Exception("Index out of range")
        
        itr = self.head
        count = 0
        
        while itr:
            if count == index -1:
                itr.next = Node(data,itr.next)
                break 
            
            itr = itr.next
            count += 1
    
    def remove_at_index(self,index):
        if index <0 or index >= self.list_length():
            return Exception("Index out of range")
        
        if index ==0:
            self.head = self.head.next
            
        itr = self.head
        count = 0 
        
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

from collections import deque
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


           
        
if __name__ == '__main__':
    l = LinkedList()
    l.top_push(3)
    l.top_push(7)
    l.top_push(9)
    l.bottom_push(5)
    l.insert_at_index(100,2)
    l.remove_at_index(3)
    l.print_list()
    print('length is: ',l.list_length())
    
    stack = Stack()
    stack.push('hajbdd')
    stack.reversed
    print(stack.reversed())
    

                            