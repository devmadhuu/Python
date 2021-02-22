userinput = 'peter piper picked a peck of pickled peppers.\n'
index = 0
p_counter = 0
while userinput[index:]:
    if userinput[index] == 'p':
        print(index)
    index+=1