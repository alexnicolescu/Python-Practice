number = int(input("Please enter a integer number > "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
if number % 4 == 0:
    print(f"{number} is a multiple of 4")
else:
    print(f"{number} is not a multiple of 4")
num = int(input("Please enter a number to check > "))
check = int(input("Now, please enter a number to divide > "))
if num % check == 0:
    print(f"{check} devides evenly into {num}")
else:
    print(f"{check} does not devide evenly into {num}")



