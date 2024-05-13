class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_on_top(self, data):
        top = ListNode(data, self.head)
        self.head = top
        
    def insert_at_end(self, data):
        if self.head is None:
            self.head = ListNode(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = ListNode(data, None)
        
    def insert_list(self, arr):
        self.head = None
        for element in arr:
            self.insert_at_end(element)
            
   
def addTwoNumbers(ls1, ls2):
    l2 = LinkedList()
    l2.insert_list(ls2)
    l1 = LinkedList()
    l1.insert_list(ls1)
    
    dummy_head = LinkedList()
    carry = 0
    
    itr = l1.head
    itr2 = l2.head

    while itr or itr2 or carry:
        val1 = itr.val if itr else 0
        val2 = itr2.val if itr2 else 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        dummy_head.insert_at_end(total_sum % 10)
        
        if itr:
            itr = itr.next
        if itr2:
            itr2 = itr2.next
    item = dummy_head.head
    answerlist = []
    while item:
        answerlist.append(item.val)
        item = item.next
        
    return answerlist

if __name__ == '__main__':
    print(addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))
