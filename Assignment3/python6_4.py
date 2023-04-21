'''Write a Python script to check if a given key already exists in a dictionary. '''

from python6_3 import concatinate
# fruit_quantity={'apple':5,'kiwi':1,'mango':8,'Lemon':2,'Pear':10,'Atlantic giant pumpkin':1}

d=100

def exist(fruits,key):
    if key in fruits:
        return f'key {key} is already present with value'
    else:
        return f'key {key} is not present'
print(exist(concatinate({5:50,6:60}, {3:30, 4:40}, {1:10, 2:20}), d))