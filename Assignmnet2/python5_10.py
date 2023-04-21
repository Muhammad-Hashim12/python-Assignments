'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
'''
user_salary=int(input('enter the salary: '))
user_total_exp=int(input('enter the total experiance: '))

total_salary=user_salary
if user_total_exp>5:
    total_salary=user_salary+(user_salary*5/100)
print(total_salary)

