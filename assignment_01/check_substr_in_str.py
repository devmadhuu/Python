## Program to check if a Substring is Present in a Given String:
main_str = input ('Enter main string to check substring :')
sub_str = input ('Enter substring :')
if main_str.index(sub_str) > 0:
    print('"{sub_str}" is present in main string - "{main_str}"'.format(sub_str = sub_str, main_str = main_str))
