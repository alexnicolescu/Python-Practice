#Write a Python program to square and cube every number in a given list of integers using Lambda.
my_list = [2, 4, 9, 3, 1, 0, -3, -4, -9, 10, 9, 4]
squares = list(map(lambda x: x * x, my_list))
cubes = list(map(lambda x: x * x * x, my_list))
print(squares)
print(cubes)