'''Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

def dict_range(dic={}):
    # for num in range(1,5+1):
    #     dic.update({num:num*num})
    dic={num:num*num for num in range(1,5+1)}
    return dic
dictprint=dict_range()     
print(dictprint)  
