'''Take 10 integers from keyboard using loop and print their average value on the screen.
'''
total_sub=10
count=1
total_mark=0
while count<=total_sub:
    marks=int(input('enter the mark: '))
    total_mark+=marks
    count+=1
print(f'The average mark is {total_mark/count}')

