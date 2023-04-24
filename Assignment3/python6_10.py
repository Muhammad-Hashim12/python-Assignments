'''Write a Python program to remove a key from a dictionary. '''

from python6_1 import fruit_quantity




def remove_key(fruit_quantity):
    print(fruit_quantity)
    del fruit_quantity["Atlantic giant pumpkin"]
    del fruit_quantity["Lemon"]
    return fruit_quantity

removing =remove_key(fruit_quantity)

if __name__ == "__main__" :
    print(removing)