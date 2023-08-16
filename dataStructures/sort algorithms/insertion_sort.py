def main():
    array = [15,12,27,20,88,23,14,7]
    print(insertionsort(array))
    
def insertionsort(array):
    for i in range(1,len(array)):
        anchor = array[i]
        
        j = i -1
        
        while j >= 0 and anchor < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = anchor
        
    return array

if __name__ =='__main__':
    main()