## Program to do number comparison

num1 = input('Enter first number :')
if num1.isdigit() or (num1.count('-') == 1 and num1.index('-') == 0) or num1.count('.') == 1:
    num2 = input('Enter second number:')
    if num2.isdigit() or (num2.count('-') == 1 and num2.index('-') == 0) or num2.count('.') == 1:
        if num1.count('.') == 1 or num2.count('.') == 1:
            operand1 = float(num1)
            operand2 = float(num2)
        else:
            operand1 = int(num1)
            operand2 = int(num2)
        if operand1 > operand2:
            print('{operand1} is greater than {operand2}'.format(operand1 = operand1, operand2 = operand2))
        elif operand1 < operand2:
            print('{operand1} is smaller than {operand2}'.format(operand1 = operand1, operand2 = operand2))
        else:
            print('{operand1} is equal to {operand2}'.format(operand1 = operand1, operand2 = operand2))
    else:
        print('Enter valid numeric input')
else:
    print('Enter valid numeric input')