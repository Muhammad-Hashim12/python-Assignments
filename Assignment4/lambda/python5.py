'''Write a Python program to check whether a given string is number or not using Lambda. '''

check_num=lambda x:x.isnumeric()

def is_number(value):
    return check_num(value)
    

inp="1234"
print(is_number(inp))