## W. A P. to implement calculator but the operation to be done and two
## numbers will be taken as input from user:- Operation console should show below:-
##Please select any one operation from below:-
    ##1. To add enter 1
    ##2. to subtract enter 2
    ##3. To multiply enter 3
    ##4. To divide enter 4
    ##5. To divide and find quotient enter 5
    ##6. To divide and find remainder enter 6
    ##7. To find num1 to the power of num2 enter 7
    ##8. To Come out of the program enter 8

num1 = input('Enter first number :')
if num1.isdigit() or (num1.count('-') == 1 and num1.index('-') == 0) or num1.count('.') == 1:
    num2 = input('Enter second number:')
    if num2.isdigit() or (num2.count('-') == 1 and num2.index('-') == 0) or num2.count('.') == 1:
        print('Please select any one operation from below:')
        print(' To add enter 1 \n To subtract enter 2 \n To multiply enter 3 \n To divide enter 4 \n To divide and find quotient enter 5 \n To divide and find remainder enter 6 \n To find num1 to the power of num2 enter 7 \n To Come out of the program enter 8')
        operation = input()
        result = 0
        operand1 = 0
        operand2 = 0
        error = 0
        if num1.count('.') == 1 or num2.count('.') == 1:
            operand1 = float(num1)
            operand2 = float(num2)
        else:
            operand1 = int(num1)
            operand2 = int(num2)
        if operation == '1':
            result = operand1 + operand2
        elif operation == '2':
            result = operand1 - operand2
        elif operation == '3':
            result = operand1 * operand2
        elif operation == '4':
            if operand2 == 0:
                error = 1
                print('Division by zero not allowed !!!')
            else:
                result = operand1 / operand2
        elif operation == '5':
            if operand2 == 0:
                error = 1
                print('Division by zero not allowed !!!')
            else:
                result = operand1 // operand2
        elif operation == '6':
            if operand2 == 0:
                error = 1
                print('Division by zero not allowed !!!')
            else:
                result = operand1 % operand2
        elif operation == '7':
            result = operand1 ** operand2
        elif operation == '8':
            pass
        if operation != '8' and error != 1:
            print ('Result is : {result}'.format(result = result))
    else:
        print('Enter valid numeric input')
else:
    print('Enter valid numeric input')