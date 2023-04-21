'''From the two list obtained in previous question, make new lists, 
containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.'''


even_list=[]
odd_list=[]
new_even_list=[]
new_odd_list=[]
for num in range(1,101+1):
    if num%2==0:
        even_list.append(num)
    if num%2!=0:
        odd_list.append(num)
for i in  even_list:
    if i%4==0 or i%6==0 or i%8==0 or i%10==0:
        new_even_list.append(i)
for i in odd_list:
    if i%3==0 or i%5==0 or i%7==0 or i%9==0:
        new_odd_list.append(i)
print(new_even_list)
print(new_odd_list)

