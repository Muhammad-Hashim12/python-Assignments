'''Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''


d={0: 10, 1: 20}

def add_key(d_key,add):
    d_key.update(add)
    return d_key
print(add_key(d,{2:30}))