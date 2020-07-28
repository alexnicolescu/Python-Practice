from collections import defaultdict, Counter


def count1(my_string):
    my_string = my_string.split()
    my_dict = defaultdict(int)
    for element in my_string:
        my_dict[element] += 1
    return my_dict


def count2(my_string):
    my_string = my_string.split()
    my_string = [element for element in my_string if element.isnumeric()]
    my_counter = Counter(my_string)
    least_common = my_counter.most_common()
    least_common = least_common.reverse()
    return least_common

if __name__ == "__main__":
    print(count1("5 3 2 1 4 2 5"))
    print(count2("5 3 2 1 4 2 5"))
