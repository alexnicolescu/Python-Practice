num = int(input("Enter a number > "))
print([element for element in range(1, num + 1) if num % element == 0])