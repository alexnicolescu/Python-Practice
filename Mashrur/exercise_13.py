from random import randint


lenght_of_a = randint(5, 40)
lenght_of_b = randint(5, 40)
a = [randint(0, 50) for iteration in range(lenght_of_a)]
b = [randint(0, 50) for iteration in range(lenght_of_b)]
a = list(set(a))
b = list(set(b))
c = [element for element in a if element in b]
c.sort()
print("New list {}".format(c))
