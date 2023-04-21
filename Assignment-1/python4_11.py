'''Write a Python function to reverses a string if it's length is a multiple of 4. '''


string='hashim12'

def reverse(string):
    if len(string)%4==0:
        return string[::-1]
print(reverse(string))