## W. A P. which takes one number from 0 to 9 from the user and prints it
## in the word. And if the word is not from 0 to 9 then it should print that
## number is outside of the range and program should exit.

userinput = input('Please enter number between 0 to 9 :')
if userinput.isdigit():
    num = int(userinput)
    if num == 0:
        print ('Zero')
    elif num == 1:
        print ('One')
    elif num == 2:
        print ('Two')
    elif num == 3:
        print ('Three')
    elif num == 4:
        print ('Four')
    elif num == 5:
        print ('Five')
    elif num == 6:
        print ('Six')
    elif num == 7:
        print ('Seven')
    elif num == 8:
        print ('Eight')
    elif num == 9:
        print ('Nine')
else:
    print('Number is outside of range !!!')