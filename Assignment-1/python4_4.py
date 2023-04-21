'''Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : resta$t'''

string='restart'
new_string=''
for index in range(len(string)):
    if string[index]==string[0] and index!=0:
        new_string+='$'
    else:
        new_string+=string[index]
print(new_string)


#another way
'''string='restart'
char=string[0]
new_string=char+string[1::].replace(char,'$')
print(new_string)'''