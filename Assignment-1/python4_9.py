'''Write a Python program to remove the nth index character from a nonempty string.'''

string='muhammad isthifa'
def remove_nth(string,n):
    return string[:n:]+string[n+1::]
print(remove_nth(string,11))

