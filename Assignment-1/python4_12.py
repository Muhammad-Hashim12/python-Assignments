''' Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
'''
string='HAshim'
# def convert_upper(string):
def convert(string):
    new_str=string[:4:]
    count=0
    for char in new_str:
        if char.isupper():
            count+=1
    if count>=2:
        return string
print(convert(string))


        
