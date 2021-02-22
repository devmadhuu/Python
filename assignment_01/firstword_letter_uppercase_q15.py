userinput = 'Peter Piper Picked A Peck Of Pickled Peppers.'
words = userinput.split()
updated_words = ''
index = 0
while index <= len(words) - 1:
    if index != 0:
        updated_word = words[index][0].lower() + words[index][1:]
    else:
        updated_word = words[index]
    updated_words+=updated_word + ' '
    index+=1
print(updated_words)