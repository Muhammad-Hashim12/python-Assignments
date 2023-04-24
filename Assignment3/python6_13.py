'''Write a Python program to remove duplicates from Dictionary.'''

from python6_1 import fruit_quantity

unique_dic={}

def duplicate_dic(fruit_quantity):
    for key,value in fruit_quantity.items():
        if value not in unique_dic.values():
            unique_dic[key]=value
    return unique_dic
print(duplicate_dic(fruit_quantity))
