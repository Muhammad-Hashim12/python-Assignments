'''Write a Python program to check a dictionary is empty or not.''' 

from python6_1 import fruit_quantity

'''def dic_empty(fruit_quantity):
    if len(fruit_quantity)>1:
        print("dictionary is not empty")
    else:
        print('dictionary is empty')
dic_empty(fruit_quantity)'''


d={}
def dic_empty(d):
    if not bool(d):
        print("dictionary is empty")
    else:
        print("dictionary is not empty")

dic_empty(d)