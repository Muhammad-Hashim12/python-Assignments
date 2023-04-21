'''Write a Python program to multiply all the items in a dictionary.'''


from python6_7 import merge_dic

def mul_al(dict_value):
    result=1
    for key in dict_value:
        result*=dict_value[key]
    return result
print(mul_al(merge_dic))
