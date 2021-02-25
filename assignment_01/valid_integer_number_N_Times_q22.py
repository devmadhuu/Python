num = 0
allowed_times = 0
while True:
    userinput = input('Enter valid integer :')
    if userinput.replace('-','').isalpha():
        print('Please enter valid integer !!!')
        allowed_times+=1
        if allowed_times == 5:
            break
        continue
    if userinput.isdigit() or (userinput.count('-') == 1 and userinput.index('-') == 0) or userinput.count('.') == 1:
        if userinput.count('.') == 1:
            num = float(userinput)
        else:
            num = int(userinput)
        print('{} is a valid integer'.format(num))
    else:
        print('Please enter valid integer !!!')
        allowed_times+=1
        if allowed_times == 5:
            break
        continue