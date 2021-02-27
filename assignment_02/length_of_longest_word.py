userinput = 'Python is very powerful language understooooooooooooood...........'
words = userinput.split()
longest_word_len = len(words[0])
longest_word = words[0]
for word in words:
    if longest_word_len < len(word):
        longest_word_len = len(word)
        longest_word = word
print(longest_word , longest_word_len)