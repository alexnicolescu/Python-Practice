from re import sub
from collections import Counter


def word_count(word_to_look_for ,path="pg100.txt"):
    with open(path, "r") as file:
        count = 0
        list_of_lines = file.readlines()
        list_of_lines = [sub(r"[?.:,!*\[\]]"," ", x) for x in list_of_lines]
        text = " ".join(list_of_lines)
        list_of_words = text.split()
        list_of_words = [word.lower() for word in list_of_words]
        for word in list_of_words:
            if word == word_to_look_for:
                count += 1
        print(f"{word_to_look_for}:{count}")


word_count("library")