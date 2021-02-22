## Program to do number comparison

num1 = input('Enter first number :')
if num1.isdigit() or (num1.count('-') == 1 and num1.index('-') == 0) or num1.count('.') == 1:
    num2 = input('Enter second number:')
    if num2.isdigit() or (num2.count('-') == 1 and num2.index('-') == 0) or num2.count('.') == 1:
        num3 = input('Enter third number:')
        if num3.isdigit() or (num3.count('-') == 1 and num3.index('-') == 0) or num3.count('.') == 1:
            if num1.count('.') == 1 or num2.count('.') == 1 or num3.count('.') == 1:
                operand1 = float(num1)
                operand2 = float(num2)
                operand3 = float(num3)
            else:
                operand1 = int(num1)
                operand2 = int(num2)
                operand3 = int(num3)
            print('{operand1} is greater than {operand2} and {operand3}'.format(operand1 = operand1, operand2 = \
                                                                                operand2, operand3 = operand3)) \
            if operand1 > (operand2 and operand3) else print('{operand2} is greater than {operand1} and {operand3}'.format(operand1 = operand1, \
                                                                                             operand2 = operand2, operand3 = operand3)) \
            if operand2 > (operand1 and operand3) else print('{operand3} is greater than {operand1} and {operand2}'.format(operand1 = operand1, operand2 \
                                                                                         = operand2, operand3 = operand3))
    else:
        print('Enter valid numeric input')
else:
    print('Enter valid numeric input')