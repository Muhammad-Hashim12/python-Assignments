'''From a list containing ints, strings and floats, make three lists to store them separately'''

listt=[1,'jim',3.14,'tom',7.84,'harry',10,100,'john','wicky',9.0]
int_list=[]
float_list=[]
string_list=[]
for value in listt:
    if type(value)==int:
        int_list.append(value)
    elif type(value)==float:
        float_list.append(value)
    elif type(value)==str:
        string_list.append(value)
print(int_list)
print(float_list)
print(string_list)