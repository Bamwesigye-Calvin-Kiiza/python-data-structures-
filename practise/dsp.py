# binary search review 
def main():
    un_ordered_list =  [0,3,5,6,7,9,10,15,22,30,81,101] 
    number = get_number()
    
    # print(binarysearch(un_ordered_list,number))
    # print(recursivebinarysearch(un_ordered_list,number,len(un_ordered_list),0))
    
# function for getting number to search for 
def get_number():
    return int(input('What number do you want to look for: '))

# binary search implementation
def binarysearch(array, number):
    left_index = 0
    right_index = len(array)-1
    middle_index = 0
    
    while left_index <= right_index:
        middle_index = (right_index + left_index)//2 
        
        if array[middle_index] == number:
            return f'{number} is at the {middle_index}th index'
        
        if array[middle_index] > number :
            right_index = middle_index-1
            
        else:
            left_index = middle_index+1
        
    return f'{number} does not exist in the list'

# recursive binary search 
def recursivebinarysearch(array,number,right_index,left_index):
    if right_index < left_index:
        return -1
    
    middle_index = (right_index+left_index)//2
    
    if middle_index >= len(array) or middle_index < 0: 
        return f'{number} does not exist in the list'
    
    if array[middle_index] == number:
        return f'{number} is at the {middle_index}th index'
    
    if array[middle_index] > number :
        right_index = middle_index-1         
    else:
        left_index = middle_index+1
    return recursivebinarysearch(array,number,right_index,left_index)
    
    
if __name__ == '__main__':
    main()