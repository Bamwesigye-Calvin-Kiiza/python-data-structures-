def main():
    array = [15,12,27,20,88,23,14,7]
    print(bubblesort(array))
    
    
def bubblesort(array):
    for i in range(len(array)-1):
        swapped = False 
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                x  = array[j]
                array[j] = array[j+1] 
                array[j+1] = x 
                swapped = True 
        if not swapped:
            break
                
    return array 

if __name__ =='__main__':
    main()