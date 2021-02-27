## WAP to check if this tuple (20, 20, 30, 30, 30, 40, 40, 40, 10) is in
## ascending/ descending or in random order without inbuilt function.

num_tuple =  (67, 75, 78, 88, 98, 111)
#num_tuple =  (60, 50, 40, 35, 25, 20, 15, 10, 5)
num_of_items = len(num_tuple)
smallest_num = num_tuple[0]
sort_type = ''
for num in num_tuple:
    if smallest_num <= num:
        sort_type = 'Ascending'
        continue
    elif smallest_num > num:
        #print(smallest_num, num)
        if sort_type == 'Ascending':
            sort_type = 'Random'
        else:
            sort_type = 'Descending'
print(sort_type)