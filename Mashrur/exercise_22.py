def reverse_word_order(given_string):
    words_list = given_string.split()
    words_list = list(reversed(words_list))
    new_string = " ".join(words_list)
    return new_string


given_string = "My name is Michele"
print(reverse_word_order(given_string))