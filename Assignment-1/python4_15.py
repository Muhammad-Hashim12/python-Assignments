''' Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
'''

string='thequickbrownfoxjumpsoverthelazydog'
dictionary={}
for char in string:
    if char in dictionary:
        dictionary[char]+=1
    else:
        dictionary[char]=1


for char,count in dictionary.items():
    if count > 1:
        print(char,count)
