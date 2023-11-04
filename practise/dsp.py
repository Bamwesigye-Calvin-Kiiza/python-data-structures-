# binary search review 
def main():
    un_ordered_list =  [2,1,5,7,2,0,5] 
    # number = get_number()
    
    # print(binarysearch(un_ordered_list,number))
    # print(recursivebinarysearch(un_ordered_list,number,len(un_ordered_list),0))
    # print(bubblesort(un_ordered_list))
    print(insertionsort(un_ordered_list))
    
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

def bubblesort(array):
    for x in range(len(array)-1):
        shuffle = False
        
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i]= array[i+1]
                array[i+1] = tmp
                shuffle = True
                
        if shuffle == False:
            break

    return array     

def insertionsort(array):
    for i in range(1,len(array)):
        pivot = array[i]
        sorted_array_index = i -1 
        
        while sorted_array_index >=0 and pivot < array[sorted_array_index]:
            array[sorted_array_index + 1] = array[sorted_array_index]
            sorted_array_index -= 1
        array[sorted_array_index+1] = pivot 
        
    
        
       
    return array
    
if __name__ == '__main__':
    main()