# Write a Python program that sum the length of the names of a given list of names after removing the names that starts with an lowercase letter. Use lambda function.
my_list = ['dan', 'Ban', 'Man', 'Ran']
my_list = list(filter(lambda x: x[0].isupper(), my_list))
print(len("".join(my_list)))
