'''Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

"""s='google.com'
result={}
for i in s:
    result[i]=s.count(i)
print(result)"""

# other way
s='google.com'
dictionary={}
for char in s:
    if char in dictionary:
        dictionary[char]+=1
    else:
        dictionary[char]=1
print(dictionary)


