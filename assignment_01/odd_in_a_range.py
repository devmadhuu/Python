## Program to print Odd number within a given range.
start = input ('Enter start number of range:')
end = input ('Enter end number of range:')
if start.isdigit() and end.isdigit():
    start = int(start)
    end = int(end)
    if end > start:
        for num in range(start, end):
            if num % 2 != 0:
                print('Number {num} is odd'.format(num = num))
    else:
        print('End number should be greater than start number !!!')
else:
    print('Enter valid start and end range !!!')