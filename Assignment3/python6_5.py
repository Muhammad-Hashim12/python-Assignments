''' Write a Python program to iterate over dictionaries using for loops.'''

from python6_1 import fruit_quantity


'''for key,value in fruit_quantity.items():
    print(key,value)'''
    
for key in fruit_quantity:
    print(key,fruit_quantity[key])   