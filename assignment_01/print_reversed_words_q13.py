userinput = 'peter piper picked a peck of pickled peppers.'
words = userinput.split()
reversed_words = ''
index = 0
while index <= len(words) - 1:
    reversed_words+=words[index][::-1] + ' '
    index+=1
print(reversed_words)