def even1(my_list):
    return [element for element in my_list if element % 2 == 0]


def even2(my_list):
    list_of_evens = []
    for element in my_list:
        if element % 2 == 0:
            list_of_evens.append(element)
    return list_of_evens


def even3(my_list):
    return list(filter(lambda element: element % 2 == 0, my_list))


if __name__ == "__main__":
    print(even1([1, 2, 3, 4]) == [2, 4])
    print(even1([2, 4, 6, 8]) == [2, 4, 6, 8])
    print(even1([]) == [])
    print(even2([1, 2, 3, 4]) == [2, 4])
    print(even2([2, 4, 6, 8]) == [2, 4, 6, 8])
    print(even2([]) == [])
    print(even3([1, 2, 3, 4]) == [2, 4])
    print(even3([2, 4, 6, 8]) == [2, 4, 6, 8])
    print(even3([]) == [])
