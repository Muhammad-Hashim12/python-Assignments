'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''



Quantity=int(input('enter quantity of units that parchased '))
Total_cost=Quantity*100

if Quantity >1000:
    Total_cost*=0.9
print("Total cost: $",Total_cost)