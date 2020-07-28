my_string = str(input("Enter a string > "))
reversed_string = my_string[::-1]
if my_string == reversed_string:
    print("{} is a palindrome".format(my_string))
else:
    print(f"{my_string} is not a palindrome")