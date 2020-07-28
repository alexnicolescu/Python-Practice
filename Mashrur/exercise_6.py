def flatten1(my_list, depth):
    my_new_list = []
    for element in my_list:
        if type(element) is list and depth != 0:
            my_new_list.extend(flatten1(element, depth - 1))
        else:
            my_new_list.append(element)
    return my_new_list


def flatten2(my_list, depth):
    if depth <= 0:
        return my_list
    while depth != 0:
        my_new_list = []
        for element in my_list:
            if type(element) == list:
                my_new_list += element
            else:
                my_new_list += [element]
        depth -= 1
        my_list = my_new_list
    return my_new_list


if __name__ == "__main__":
    print(flatten1([1, 4], 1) == [1, 4])
    print(flatten1([1, 4], 0) == [1, 4])
    print(flatten1([4, 2, [3], 5], 1) == [4, 2, 3, 5])
    print(flatten1([1, 2, [3, [4]]], 2) == [1, 2, 3, 4])
    print(flatten1([1, 2, [3, [4]]], 1) == [1, 2, 3, [4]])

    print(flatten2([1, 4], 1) == [1, 4])
    print(flatten2([1, 4], 0) == [1, 4])
    print(flatten2([4, 2, [3], 5], 1) == [4, 2, 3, 5])
    print(flatten2([1, 2, [3, [4]]], 2) == [1, 2, 3, 4])
    print(flatten2([1, 2, [3, [4]]], 1) == [1, 2, 3, [4]])

    my_list = [1, 2, 3, [4, [5]]]
    flatten2(my_list, 1)
    print(my_list)
