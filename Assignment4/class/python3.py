'''Write a Python class to get all possible unique subsets from a set of distinct integers
 Input : [4, 5, 6]
 Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''

class UniqueSubSet:

    def subset(self,col):
        l=[[]]
        for i in range(len(col)+1):
            for j in range(i):
                l.append(col[j:i])
        print(l)

        
distict_int=UniqueSubSet()

distict_int.subset([4,5,6])

