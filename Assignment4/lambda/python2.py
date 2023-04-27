'''Write a Python program to sort a list of tuples using Lambda. 
Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''


sort_list=lambda x:x[1]


def sorting(listt):
    listt.sort(key=sort_list)
    return listt
l=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(sorting(l))