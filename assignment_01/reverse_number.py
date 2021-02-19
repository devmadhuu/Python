## Program to reverse a given number.
userinput = input ('Enter number to do the reverse :')
if userinput.isdigit() or userinput.find('-') >= 0:
    reverse_num = userinput[::-1]
    print ('Reverse of {a} is {reverse_num}'.format(a = userinput, reverse_num = reverse_num))
else:
    print('Enter valid numeric input')