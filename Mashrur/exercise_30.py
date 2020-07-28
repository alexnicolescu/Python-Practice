from random import choice


def get_words_list():
    with open("sowpods.txt", "r") as f:
        return [word.strip() for word in f]


words_list = get_words_list()
print(choice(words_list))