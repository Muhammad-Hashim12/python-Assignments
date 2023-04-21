'''Write a Python program that counts the number of elements within a list that are greater than 30.
'''


def counting(listt,count=0):
    for num in listt:
        if num>30:
            count+=1
    return count
print(counting([100,68,40,80,20,10,5,15]))