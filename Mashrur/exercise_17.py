from random import randint


guess_number = 0
solution = randint(1, 9)
while True:
    user_input = str(input("Enter a integer number between 1 and 9 or type exit to stop this game > "))
    if user_input == "exit":
        break
    num = int(user_input)
    guess_number += 1
    if num == solution:
        print("Exactly right!")
        break
    elif num < solution:
        print("Too low!")
    else:
        print("Too high!") 
print(f"Number of guesses {guess_number}")
    