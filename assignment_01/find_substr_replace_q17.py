my_str = 'Peter Piper Picked A Peck Of Pickled Peppers.'
sub_str = 'Peck'
new_str = 'Pack'
index = 0
str_index = -1
replaced_str = ''
while my_str[index:]:
    check_str = my_str[index:index + len(sub_str)]
    if check_str == sub_str:
        replaced_str = my_str[0:index] + new_str
        replaced_str+=my_str[index + len(sub_str):]
        break
    index+=1
if replaced_str != '':
    print(replaced_str)
else:
    print('"{sub_str}" substring not found'.format(sub_str = sub_str))