# Write a Python program to sort a list of tuples using Lambda.
my_list = [(2, 1),(4, 3), (1, 8), (3, 9), (6, 7), (0 ,3)]
my_list.sort(key = lambda x: x[0])
print(my_list)