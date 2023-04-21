'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.'''

user1_sub1=int(input('enter the marks1: '))
user1_sub2=int(input('enter the marks2: '))
user1_sub3=int(input('enter the marks3: '))
user1_sub4=int(input('enter the marks4: '))
user1_sub5=int(input('enter the marks5: '))
user1_sub6=int(input('enter the marks6: '))

def grade(marks):
    if marks<25:
        print(marks," F")
    elif marks>=25 and marks<45:
        print(marks," E")
    elif marks>=45 and marks<50:
        print(marks," D")
    elif marks>=50 and marks<60:
        print(marks," C")
    elif marks>=60 and marks<80:
        print(marks," B")
    elif marks>=80:
        print(marks," A")
grade(user1_sub1)