''' Write a Python program to remove all consecutive duplicates of a given string.'''

string='successive'
new_string=''
for i in range(0,len(string)):
    if i==0 or string[i]!=string[i-1]:
        new_string+=string[i]
print(new_string)