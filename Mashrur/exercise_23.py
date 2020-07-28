from random import randint, choice


seq = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?.,"
pass_length = randint(10, 20)
password = "".join([choice(seq) for iteration in range(pass_length)])
print(password)
