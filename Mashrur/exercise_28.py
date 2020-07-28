def generate_list(file):
    with open(file, "r") as f:
        return [int(num) for num in f]


def get_overlapping_numbers(list_1, list_2):
    return [num for num in list_1 if num in list_2]


prime_numbers_list = generate_list("primenumbers.txt")
happy_numbers_list = generate_list("happynumbers.txt")
print(get_overlapping_numbers(prime_numbers_list, happy_numbers_list))