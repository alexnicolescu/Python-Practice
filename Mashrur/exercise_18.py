from random import sample, randint
lenght_of_a = randint(5, 40)
lenght_of_b = randint(5, 40)
a = sample(range(1, 50), lenght_of_a)
b = sample(range(1, 50), lenght_of_b)
print([element for element in a if element in b])