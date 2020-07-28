def prime_check(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True


num = int(input("Enter a number > "))
if prime_check(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
