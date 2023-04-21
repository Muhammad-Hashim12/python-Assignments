'''Write a Python program to sum all the items in a dictionary.'''

from python6_7 import merge_dic


def sum_all(dict_value):
    result=0
    for key in dict_value:
        result+=dict_value[key]
    return result
total=sum_all(merge_dic)
print(total)
    

