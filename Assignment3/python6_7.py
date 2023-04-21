''' Write a Python script to merge two Python dictionaries.'''

dict1 = {'apple': 1, 'banana': 2}
dict2 = {'orange': 3, 'kiwi': 4}

merge_dic={**dict1,**dict2}

if __name__ == '__main__' :
    print(merge_dic)



