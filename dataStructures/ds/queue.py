from collections import deque


class Queue():
    '''
    class to handle queues methods and implementations
    '''
    def __init__(self):
        self.container = deque()
        
    def enqueue(self,value):
        '''
        add a value to the left side of the queue
        '''
        return self.container.appendleft(value)
    
    def form_queue(self,value):
        '''
        turn provided data into a queue
        '''
        for letter in value:
            self.enqueue(letter)
        
    
    def deque(self):
        '''
        remove item that is on the right side of the queue
        '''
        return self.container.pop()
    
    def peek(self):
        '''
        return the top value of the queue
        '''
        return self.container[-1]
    
    def size(self):
        '''
        returns length of the queue
        '''
        return len(self.container)
    
    def print_queue(self):
        '''
        print queue contents
        '''
        strr = []
        for letter in  self.container:
            strr.append(letter)
        return strr
    
    def is_empty(self):
        '''
        check whether queue is empty
        '''
        return len(self.container) == 0
    

if __name__ == '__main__':
        queue = Queue()
        name = 'queue'
        queue.form_queue(name)
        print(queue.size())
        print(queue.peek())
        print(queue.print_queue())
        queue.deque()
        print(queue.print_queue())
        q = Queue()
        q.enqueue({
            'company': 'Wall Mart',
            'timestamp': '15 apr, 11.01 AM',
            'price': 131.10
        })
        q.enqueue({
            'company': 'Wall Mart',
            'timestamp': '15 apr, 11.02 AM',
            'price': 132
        })
        q.enqueue({
            'company': 'Wall Mart',
            'timestamp': '15 apr, 11.03 AM',
            'price': 135
        })
        print(q.print_queue())