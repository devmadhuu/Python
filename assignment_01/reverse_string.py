## Reverse string
userinput = input ('Enter string to do the reverse :')
index_pos = len(userinput) - 1
reversed_string = ''
while index_pos >= 0:
    reversed_string+=userinput[index_pos]
    index_pos-=1
print('Reverse of {userinput} is {reversed_string}'.format(userinput = userinput,reversed_string = reversed_string))