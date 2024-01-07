from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()
    
    def enqueue(self,data):
        self.container.appendleft(data)
        
    def dequeue(self):
        self.container.pop()
        
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
if __name__ == '__main__':
    q = Queue()
    q.enqueue(3)
    q.enqueue(7)
    pq = Queue()

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
print(q.is_empty())