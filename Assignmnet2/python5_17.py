'''Using range(1,101), make three list, 
one containing all even numbers
one containing all odd numbers 
One containing only prime numbers..'''

even_list=[]
odd_list=[]
prime_list=[]
for num in range(1,101+1):
    if num%2==0:
        even_list.append(num)
    if num%2!=0:
        odd_list.append(num)
    for i in range(2,num):
        if num%i==0:
            break
    else:
        prime_list.append(num)
print(even_list)
print(odd_list)
print(prime_list)
