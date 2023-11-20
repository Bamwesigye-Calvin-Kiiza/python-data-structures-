class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        
        # inserting a new node as the head
    def insert_at_beginning (self,data):
        node = Node(data,self.head)
        self.head = node
        
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        
        print(llstr)
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
         
        itr.next = Node(data,None)
           
    def insert_values (self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next 
        return count
            
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

            
    def insert_at(self, index, data):      
        if index < 0 or index >= self.get_length():
            raise Exception('Index out of range')
        if index == 0:
            self.insert_at_beginning(data)
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    

if __name__ =='__main__':
    ll = Linkedlist()
    ll.insert_values(['data_list','hajsvd','yudasgdua'])
    ll.print()
    print(f'Length of the linked list is: {ll.get_length()}')
    # ll.remove_at(1)
    ll.insert_at(1,'calvin')
    ll.print()