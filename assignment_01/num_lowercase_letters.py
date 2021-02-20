## Count Number of Lowercase Characters in a String:
userinput = input ('Enter string to check number of lowercase letters in a string:')
num_lowercase = 0
index_pos = 0
while index_pos < len(userinput):
    if userinput[index_pos].islower():
        num_lowercase+=1
    index_pos+=1
print("Number of lowercase letters in : {userinput} is {num_lowercase}".format(userinput = userinput, num_lowercase = num_lowercase))