'''Write a Python program to construct the following pattern, using a nested loop number.
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
for row in range(1,10):
    for col in range(1,row+1):
        print(row,end='')
    print()
    