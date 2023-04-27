'''Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda 
Orginal list: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190] 
Numbers of the above list divisible by nineteen or thirteen: [19, 65, 57, 39, 152, 190] '''


divisible=lambda x: x%19==0 or x%13==0


listt=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190,1]

result=filter(divisible,listt)
print(list(result))