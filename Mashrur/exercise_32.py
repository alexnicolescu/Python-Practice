from random import choice


def get_words_list():
    with open("sowpods.txt", "r") as f:
        return [word.strip() for word in f]


def check_letter(word, sol, given_letter):
    for index, letter in enumerate(word):
        if given_letter == letter:
            sol[index] = given_letter


while True:
    words_list = get_words_list()
    word = choice(words_list)
    used_letters = []
    solution = ['_'] * len(word)
    lives = 6
    while lives != 0:
        letter = str(input("Enter a letter >>> "))[0].upper()
        if letter in used_letters:
            print("Letter already used!")
        else:
            used_letters.append(letter)
            if letter in word:
                check_letter(word, solution, letter)
                print(solution)
                if not '_' in solution:
                    break
            else:
                print("Wrong letter!")
                lives -= 1
                print("You have {} lives left".format(lives))
    if lives == 0:
        print("You lost!")
        print(f"{word} was the solution")
    else:
        print("You won!")
    again = str(input("Wanna play again?Type yes or no >>> "))[0].lower()
    if again == 'n':
        break
