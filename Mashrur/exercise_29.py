from random import randint


guesses = 0
num = 50
while True:
    print(f"Is {num} the correct number?")
    response = str(input(">>> "))
    guesses += 1
    if response == "too high":
        num -= randint(1, 5)
    elif response == "too low":
        num += randint(1, 5)
    else:
        print(f"Correct! It took you {guesses} guesses")
        break