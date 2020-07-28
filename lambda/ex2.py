# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def multiply(n):
    return lambda x: x*n


result = multiply(2)
print(result(3))
