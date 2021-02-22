userinput = 'peter piper picked a peck of pickled peppers.'
words = userinput.split()
reversed_words = ''
index = len(words) - 1
while index >= 0:
    reversed_words+=words[index][::-1] + ' '
    index-=1
print(reversed_words)
