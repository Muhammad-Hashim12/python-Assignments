'''Print multiplication table of 24, 50 and 29 using loop.
'''

a=24
b=50
c=29
for i in range(1,10+1):
    print(f'{a}*{i}={a*i}',end='   ')
    print(f'{b}*{i}={b*i}',end='   ')
    print(f'{c}*{i}={c*i}',end='   ')
    print()
