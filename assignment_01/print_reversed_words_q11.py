userinput = 'peter piper picked a peck of pickled peppers.'
words = userinput.split()
reversed_words = ''
index = len(words) - 1
words[index] = words[index][:-1] ## remove dot at end
while index >= 0:
    reversed_words+=words[index] + ' '
    index-=1
print(reversed_words)