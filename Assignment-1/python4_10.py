''' Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white'''


listt=['red', 'white', 'black', 'red', 'green', 'black']
def re_arrange(listt):
    new_list=[]
    for word in listt:
        if word not in new_list:
            new_list.append(word)
    new_list.sort()
    return new_list
print(re_arrange(listt))