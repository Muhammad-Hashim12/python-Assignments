'''
Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda. 
Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
 Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]] 
Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
'''

listt=[[1, 2, 3], [2, 4, 5], [1, 1, 1]] 
listt2=[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sum_list=lambda x:sum(x)

def summing(l):
    l.sort(key=sum_list)
    return l
print(summing(listt2))
