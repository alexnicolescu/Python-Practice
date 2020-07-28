def eliminate_dups(given_list):
    return list(set(given_list))


a = [1, 2, 3, 4, 1, 5, 9, 2, 4, 1, 2, 3, 4]
print(eliminate_dups(a))
