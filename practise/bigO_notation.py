list_a = [1,2,3,4,5,7,6,7,3,2]

# function to detect duplicates in a given list or array.
def duplicate_detector(array):
    for a in range(len(array)):
        for i in range(a+1,len(array)):
            if array[a] == array[i]:
                print(f'{array[a]} has a duplicate')
                
duplicate_detector(list_a)