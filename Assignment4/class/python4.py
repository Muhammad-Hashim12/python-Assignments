'''
Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
 Note: There will be one solution for each input and do not use the same element twice.
 Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4 
 '''

class FindPairs:

    def pairs_element(self,col,target):
        for num in range(len(col)-1):
            if col[num]<target:
                if col[num]+col[num+1]==target:
                    print(num,num+1)


targeting_pairs=FindPairs()
l=[90, 20,10,40,50,60,70]
target=50
targeting_pairs.pairs_element(l, target)
        
        

