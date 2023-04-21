'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing' 
Sample String : 'string'
Expected Result : 'stringly'
'''
def edit(string):
    if len(string)>=3 and string[-3::]=='ing':
        return string+'ly'
    elif len(string)>=3 and string[-3::]!='ing':
        return string+'ing'
    else:
        return string
print(edit('string'))

