# Write a Python program that removes the positive numbers from a given list of numbers. Sum the negative numbers and print the absolute value using lambda function. Print the result.
my_list = [1, 2, 3, 4, 5, 6, -3, -5, -6]
print(abs(sum([element for element in my_list if element < 0])))

