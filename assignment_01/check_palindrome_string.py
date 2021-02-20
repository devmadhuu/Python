## check palindrome string
userinput = input ('Enter string to check if it is palindrome:')
index_pos = len(userinput) - 1
reversed_string = ''
while index_pos >= 0:
    reversed_string+=userinput[index_pos]
    index_pos-=1
if userinput == reversed_string:
    print('{userinput} is palindrome'.format(userinput = userinput))
else:
    print('{userinput} is not palindrome'.format(userinput = userinput))