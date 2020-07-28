# Write a Python program to sort a list of dictionaries using Lambda.
my_list = [{'a': 1}, {'c': 4}, {'d': 9}, {'e': 0}]
my_list.sort(key = lambda x: list(x.values())[0])
print(my_list)
