#Write a Python program to filter a list of integers using Lambda.
my_list = [1, -2, 4, -5, 0 , 3, 9, -9, -8, -6]
my_list = list(filter(lambda x: x >= 0, my_list))
print(my_list)