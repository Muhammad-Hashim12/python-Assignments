'''Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, 
if found. Iterate over list using for loop.'''


l=[]
for i in range(1,6):
    user_inp=input('enter any data: ')
    l.append(user_inp)
user_inp_again=input("enter value that to be deleted or press any key to continue")
if user_inp_again in l:
    l.remove(user_inp_again)
print(l)

