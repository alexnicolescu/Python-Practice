def check_letter(word, sol, given_letter):
    for index, letter in enumerate(word):
        if given_letter == letter:
            sol[index] = given_letter


word = "EVAPORATE"
used_letters = []
solution = ['_'] * len(word)
while True:
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
    