## Program is to check if a number is positive, negative or zero.
userinput = input ('Enter number to check if it is positive, negative or zero :') 
if userinput.isdigit() or userinput.find('-') >= 0:
    userinput = int(userinput)
    if userinput > 0:
        print('Number entered {a} is positive'.format(a = userinput))
    elif userinput < 0:
        print('Number entered {a} is negative'.format(a = userinput))
    else:
        print('Number entered {a} is zero'.format(a = userinput))
else:
    print('Enter valid numeric input')