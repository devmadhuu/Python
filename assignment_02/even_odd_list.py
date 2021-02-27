## Program to Put Even and Odd elements in a List into Two Different Lists:
my_list = [23, 10, 13, 43, 50, 37, 85, 87, 97, 99]
even_list = []
odd_list = []
for num in my_list:
    even_list.append(num) if num % 2 == 0 else odd_list.append(num)
print(even_list)
print(odd_list)