from random import randint


def cows_check(num, sol):
    cows = 0
    num_digits = list(str(num))
    sol_digits = list(str(sol))
    for index in range(len(num_digits)):
        if num_digits[index] == sol_digits[index]:
            cows += 1
    return cows


def bulls_check(num, sol):
    bulls = 0
    num_digits = list(str(num))
    sol_digits = list(str(sol))
    for index in range(len(num_digits)):
        if num_digits[index] != sol_digits[index] and num_digits[index] in sol_digits:
            bulls += 1
    return bulls


if __name__ == "__main__":
    sol = randint(1000, 9999)
    guess_number = 0
    while True:
        print("Enter a number:")
        num = int(input(">>> "))
        guess_number += 1
        if num == sol:
            print("Correct")
            print(f"It took you {guess_number} guesses")
            break
        print(f"{cows_check(num, sol)} cows, {bulls_check(num, sol)} bulls")
