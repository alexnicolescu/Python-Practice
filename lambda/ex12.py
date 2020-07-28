# Write a Python program to add two given lists using map and lambda.
list_1 = [1, 2, 3 ,4 ,5 ,6]
list_2 = [1, 2, 3 ,4 ,5 ,6]
list_3 = list(map(lambda x, y: x + y, list_1, list_2))
print(list_3)