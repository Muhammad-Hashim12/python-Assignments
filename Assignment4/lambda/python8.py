'''
Write a Python program to check whether a given string contains a capital letter, 
a lower case letter, a number and a minimum length using lambda.
 Minimum length : 10 input string: PaceWisd0m o/p: valid string
'''
check_str=lambda x:any(i.isupper() for i in x) and \
                    any(i.islower for i in x) and \
                    any(i.isdigit() for i in x) and \
                    len(x)>=10

user_name='PaceWisd0m'
if check_str(user_name):
    print('user_name is valid')
else:
    print('user_name is invalid')

