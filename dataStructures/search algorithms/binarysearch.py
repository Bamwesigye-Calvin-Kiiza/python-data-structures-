def main():
    list_to_be_searched = [0,3,5,6,7,9,10,15,22,30,81,101]
    number = int(input('What Number do you want to find: '))
    # print(binary_search(list_to_be_searched,number))
    print(recursive_binary_search(list_to_be_searched,number,left_index=0,right_index=len(list_to_be_searched)))
    
def binary_search(array,x):
    left_index = 0
    right_index = len(array) - 1
    middle_index = 0
    
    while left_index <= right_index:
        middle_index = (left_index + right_index)//2
        
        if array[middle_index] == x:
            return f'{x} is at index {middle_index}'
        
        if array[middle_index] > x:
             right_index = middle_index - 1
        else:
            left_index = middle_index + 1
    return -1


def recursive_binary_search(array,x,left_index,right_index):
    if right_index < left_index:
        return -1
    
    middle_index = (right_index + left_index)//2
    
    if middle_index >= len(array) or middle_index < 0:
        return -1
    
    if array[middle_index]==x:
        return f'{x} is at index {middle_index}'
    
    if array[middle_index] > x:
        right_index = middle_index - 1
    else:
        left_index = middle_index + 1
    return recursive_binary_search(array,x,left_index,right_index)


if __name__ == '__main__':
    main()