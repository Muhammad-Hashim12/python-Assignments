'''Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
 Print average and product of all numbers.
'''

i=0
count=0
value=0
product=1
while True:
    user_inp=int(input('enter the number '))
    value+=user_inp
    count+=1
    product*=user_inp
    stop_user=input('press button Q for result or press any key to continue ')
    if stop_user in 'Qq':
        break
print(f'Average value is {value/count}')
print(f'Product of value is {product}')