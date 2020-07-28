# Write a Python program to find all anagrams of a string in a given list of strings using lambda.
from collections import Counter


given_string = "bac"
my_list = ["abc", "bar", "cab", "cabb", "acb"]
anagrams = list(filter(lambda x: Counter(x) == Counter(given_string), my_list))
print(anagrams)