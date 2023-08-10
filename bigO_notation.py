list_a = [1,2,3,4,5,6,7,3,2]

for i in range(len(list_a)):
    for j in range(i+1,len(list_a)):
        if list_a[i] == list_a[j]:
            print(f'{list_a[i]} has a duplicate')