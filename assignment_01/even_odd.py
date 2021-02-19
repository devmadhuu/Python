## Program is to check if a number is Even or Odd.
userinput = input ('Enter number to check if it is even or odd:')
if userinput.isdigit() or userinput.find('-') >= 0:
    userinput = int(userinput)
    if userinput % 2 == 0:
        print('Number entered {a} is even'.format(a = userinput))
    else:
        print('Number entered {a} is odd'.format(a = userinput))
else:
    print('Enter valid numeric input')