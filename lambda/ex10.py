# Write a Python program to find intersection of two given arrays using Lambda.
array_1 = [1, 2, 3, 4]
array_2 = [3, 4, 5, 6]
intersection = list(filter(lambda x: x in array_2, array_1))
print(intersection)