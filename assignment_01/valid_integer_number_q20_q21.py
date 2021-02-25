num = 0
while True:
    userinput = input('Enter valid integer :')
    if userinput.replace('-','').isalpha():
        print('Please enter valid integer !!!')
        break
    if userinput.isdigit() or (userinput.count('-') == 1 and userinput.index('-') == 0) or userinput.count('.') == 1:
        if userinput.count('.') == 1:
            num = float(userinput)
        else:
            num = int(userinput)
        print('{} is a valid integer'.format(num))
    else:
        print('Please enter valid integer !!!')
        break