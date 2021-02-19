## Program to find out the sum of N Natural numbers.
userinput = input ('Enter number N to find sum of N natural numbers :')
if userinput.isdigit() or userinput.find('-') >= 0:
    userinput = int(userinput)
    sum_of_n = userinput * (userinput + 1) / 2
    print ('Sum of {a} natural numbers is {sum_of_n}'.format(a = userinput, sum_of_n = sum_of_n))
else:
    print('Enter valid numeric input')
