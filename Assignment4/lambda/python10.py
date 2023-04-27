'''
Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
'''
sorting_int = lambda x: type(x)==int
sorting_string=lambda x: type(x)==str

listt=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
def sorted(listt):
    sorted_int=list(filter(sorting_int,listt))
    sorted_str=list(filter(sorting_string,listt))
    sorted_int.reverse()
    sorted_str.reverse()
    return sorted_int+sorted_str

print(sorted(listt))