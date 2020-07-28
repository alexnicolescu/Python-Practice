# Write a Python program to check whether a given string is number or not using Lambda.
my_string = "1923"
is_number = lambda x: x.isnumeric()
print(is_number(my_string))
my_string = "123a"
print(is_number(my_string))
