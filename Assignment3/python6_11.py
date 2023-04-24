'''Write a Python program to sort a dictionary by key.'''

from python6_1 import fruit_quantity

def sort_key(dictionary):
    print(dictionary)
    print(sorted(dictionary.items()))

sort_key(fruit_quantity)