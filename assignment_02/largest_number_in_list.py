## find largest number in list
my_list = [23, 10, 13, 43, 50, 37, 85, 87, 97, 99]
largest = my_list[0]
for num in my_list:
    if largest < num:
        largest = num
print(largest)
#max(my_list)