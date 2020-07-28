# Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = len(list(filter(lambda x: x % 2 == 0, my_list)))
odds = len(list(filter(lambda x: x % 2 != 0, my_list)))
print(evens)
print(odds)
