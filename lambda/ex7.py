#Write a Python program to find if a given string starts with a given character using Lambda.
def find(char):
    return lambda x: x[0] == char


my_string = "abracadabra"
result = find('b')
print(result(my_string))