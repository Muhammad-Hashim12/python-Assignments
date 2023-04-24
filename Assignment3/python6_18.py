'''Write a Python program to check if all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False'''

sample_list1=[{},{},{}]

sample_list2=[{1,2},{},{}]

def empty_dic_list(x):
    for dic in x:
        if bool(dic):
            return False
    else:
        return True
print(empty_dic_list(sample_list1))

