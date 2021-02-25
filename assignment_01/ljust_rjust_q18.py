my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
index = 0
str_index = -1
replaced_str = ''
while my_str[index:]:
    check_str = my_str[index:index + len(sub_str)]
    if check_str == sub_str:
        replaced_str = sub_str.rjust(index+1, '*')
        replaced_str+=sub_str.ljust(len(my_str) - (index + 1 + len(sub_str)), '*')[len(sub_str):]
        break
    index+=1
print(replaced_str)