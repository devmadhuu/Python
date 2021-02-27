# Remove duplicate items from list
user_list = ['python', 'is' , 'is', 'a', 'very', 'very', 'powerful', 'language']
modified_list = [user_list[0]]
for word in user_list:
    if word in modified_list:
        continue
    else:
        modified_list.append(word)
print(modified_list)