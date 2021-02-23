# Write a python program to implement index method using loop. If
# sub_str is found in my_str then it will print the index of first occurrence
# of first character of matching string in my_str:-
# 1. Input: - my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.',
# 2. sub_str = 'Pickl'
# 3. Output:- 29
my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Pickl'
index = 0
str_index = -1
while my_str[index:]:
    check_str = my_str[index:index + len(sub_str)]
    if check_str == sub_str:
        str_index = index
        break
    index+=1
print(str_index)