## Count the number of digits & letter in a string:
userinput = input ('Enter string to check digits and letters:')
num_digits = 0
num_letters = 0
index_pos = 0
while index_pos < len(userinput):
    if userinput[index_pos].isdigit():
        num_digits+=1
    else:
        num_letters+=1
    index_pos+=1
print("Number of digits: {num_digits}, Number of letters: {num_letters}".format(num_digits = num_digits, num_letters = num_letters))
    