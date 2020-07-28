import random


number_of_elements = random.randint(10, 100)
numbers = []
i = 0
while i < number_of_elements:
    numbers.append(random.randint(0,100))
    i += 1
for elem in numbers:
    if elem > 90:
        print(elem)
 