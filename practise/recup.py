def main():
    list_a = [99,6,8,2,1,50,5]
    # OrderedDict = [1,2,5,6,8,50,99]
    # print(binary_search(OrderedDict,8))
    # print(bubblesort(list_a))
    # print(insertionsort(list_a))
    print(selectionsort(list_a))
    
def binary_search(array,number):
    left_index = 0
    right_index = len(array)-1
    middle_index = 0
    
    while left_index <= right_index:
        middle_index = (right_index+left_index)//2
        print(middle_index)
        if array[middle_index] == number:
            return (f'number is at index {middle_index}')
        
        if array[middle_index] > number:
            right_index = middle_index - 1
        else:
            left_index = middle_index +1 
        
    return f'{number} is not in the list'

def bubblesort(array):
    for x in range(0, len(array)-1):
        shuffle = False
        
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
            shuffle = True
        if shuffle == False:
            break 
    return array

def insertionsort(array):
    for i in range(1, len(array)):
        pivot = array[i]
        
        sorted_array_index = i-1
        
        while sorted_array_index>=0 and pivot < array[sorted_array_index]:
            array[sorted_array_index+1] = array[sorted_array_index]
            sorted_array_index -= 1
        array[sorted_array_index+1] = pivot 
    return array
    

def selectionsort (array):
    for i in range(len(array)-1):
        min_index = i
        
        for j in range(min_index+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
                
        if i != min_index:
            array[i],array[min_index] = array[min_index],array[i]
            
    return array 
            
        
if __name__ == '__main__':
    main()
    