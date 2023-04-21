'''Write a Python program to check whether a string starts with specified characters.'''


def check(string,char):
    if char ==string[0]:
        print(f'The given string {string}  starts with specified character {char}')
check('hashim','h')