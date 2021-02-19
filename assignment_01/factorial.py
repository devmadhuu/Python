## Python program to find the factorial of a number.
userinput = input ('Enter number to find the factorial:')
if userinput.isdigit() or userinput.find('-') >= 0:
    userinput = int(userinput)
    factorial = 1
    for num in range (1, userinput + 1):
        factorial*=num
    print('Factorial of {a} is {factorial}'.format(a = userinput, factorial = factorial))
else:
    print('Enter valid numeric input')