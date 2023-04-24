'''Write a Python program to get the maximum and minimum value in a dictionary. 
'''
from python6_1 import fruit_quantity

def min_max_dict(dictionary):
    d=sorted(dictionary.items(),key=lambda x: x[1])
    max_value=d[0][1]
    min_value=d[-1][1]
    return max_value,min_value
print(min_max_dict(fruit_quantity))

'''
def min_max_dict(dictionary):
    max_value=max(dictionary.values())
    min_value=min(dictionary.values())
    print(min_value,max_value)
min_max_dict(fruit_quantity)
'''