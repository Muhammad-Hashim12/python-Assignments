'''Write a Python program to match key values in two dictionaries.
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y'''

x={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}


def check_presence(x,y):
    for item in x.items():
        if item in y.items():
            print(f'{item} is present in both dictionary x and y') 
check_presence(x, y)