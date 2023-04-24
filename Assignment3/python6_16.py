'''Write a Python program to find the highest 3 values in a dictionary.'''

from python6_1 import fruit_quantity


def highest(dic):
    max_3_value=sorted(dic.values(),reverse=True)
    return max_3_value[:3:]
print(highest(fruit_quantity))


