'''Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
 replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
'''

string1 = 'The lyrics is not that poor!'
string2 = 'The lyrics is poor!'
# string='The lyrics is not that poor!'

def replace_substring(string):
    # Find the first appearance of 'not' and 'poor'
    not_index = string.find('not')
    poor_index = string.find('poor')
    
    # Check if 'not' appears before 'poor'
    if not_index < poor_index and not_index != -1 and poor_index != -1:
        # Replace the 'not'...'poor' substring with 'good'
        result = string[:not_index] + 'good' + string[poor_index+4:]
    else:
        result = string
    
    return result

result1 = replace_substring(string1)
result2 = replace_substring(string2)
print(result1)
print(result2)


