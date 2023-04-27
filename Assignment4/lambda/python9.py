''' 
Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
Original list: ['red', 'black', 'white', 'green', 'orange'] 
Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 
'''

def find_substring(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result
colors = ["red", "black", "white", "green", "orange"]


sub_str = "ack"

result=find_substring(colors, sub_str)

print(result)

