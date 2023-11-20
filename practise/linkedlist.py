class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None 
    
    def top_insert(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print_list(self):
        if self.head is None:
            raise Exception("List is empty")
            return 
        
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)
        
    def bottom_insert(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
    
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)  
        
    def convert_list(self,list_to_be_converted):
        self.head = None    
        
        for element in list_to_be_converted:
            self.bottom_insert(element)
    
    def get_length(self):
        itr = self.head
        count = 0 
        
        while itr:
            count += 1
            itr = itr.next
            
        return count  
    
    def index_insert(self,data,index):  
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
            return 
        
        if index == 0:
            self.top_insert(data)
            return
        
        itr = self.head
        count = 0 
        
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    def delete_index(self,index):  
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
            return 
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0 
        
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head 
        
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node 
                break
            itr = itr.next
            
    def remove_by_value(self,data):
        itr = self.head

        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break 
            
            itr = itr.next
                
        
if __name__ == '__main__':
    ll = linkedlist()
    lll = [8,0,5,8,2,5]
    ll.convert_list(lll)
    ll.index_insert(100, 1)
    ll.delete_index(2)
    ll.insert_after_value(8, 9)
    ll.remove_by_value(0)
    ll.print_list()
    print('length:',ll.get_length())
    