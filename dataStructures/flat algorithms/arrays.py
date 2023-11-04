expenditure_per_month = list((2200,2350,2600,2130,2190,2000))
print(expenditure_per_month)

#  task one
extra_dolars = expenditure_per_month[1]-expenditure_per_month[0]
print(f'Extra dolars spent in feb than in jan : ${extra_dolars}')

# total expenses 
expenses_in_first_quarter = expenditure_per_month[0]+expenditure_per_month[1]+ expenditure_per_month[2]
print(f'expenditure in first quarter: {expenses_in_first_quarter}')


# or 
sum = 0 
for index in range(3):
    sum += expenditure_per_month[index]  
print(f'sum: {sum}')

# task 3 
array = []
for index in range(len(expenditure_per_month)):
    if expenditure_per_month[index] == 2000:
        array.append(index)
    else:pass
months = ['jan','feb','march','april','may','june']       

if len(array)==0:
    print('no month')
else:
    print(f'month is at {months[array[0]]}')
    
# task four 
# adding july 
# expenditure_per_month.append(1980)
print(expenditure_per_month)

# task 5
# expenditure_per_month[3] = expenditure_per_month[3] - 200
print(expenditure_per_month)