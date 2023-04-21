''' Take values of length and breadth of a rectangle from user and check if it is square or not.
'''
def check_square(length,breadth):
    if length==breadth:
        print('it is square')
    else:
        print('it is not a square')
check_square(int(input('enter the length value: ')),int(input('enter the breadth value: ')))