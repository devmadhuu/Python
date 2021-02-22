userinput = 'peter piper picked a peck of pickled peppers.'
words = userinput.split()
reversed_words = ''
index = 0
while index <= len(words) - 1:
    updated_word = words[index][0].upper() + words[index][1:]
    reversed_words+=updated_word + ' '
    index+=1
print(reversed_words)