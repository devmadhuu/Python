## Python Program to Count the Number of Vowels in a String Input Two
## Strings and Display the Larger String without Using Built-in Functions:

userinput1 = input ("Enter first string to to check number of vowels :")
userinput2 = input ("Enter second string to to check number of vowels :")
vowelchars = "aeiou"
index1 = 0
index2 = 0
str1vowelcount = 0
str2vowelcount = 0
while index1 < len(userinput1):
    if userinput1[index1] in vowelchars:
        str1vowelcount+=1
    index1+=1
while index2 < len(userinput2):
    if userinput2[index2] in vowelchars:
        str2vowelcount+=1
    index2+=1
userinput1 if str1vowelcount > str2vowelcount else userinput2 if str2vowelcount > str1vowelcount else "Both strings have equal vowel count"