'''Write a Python class to find the three elements that sum to zero from a set of n real numbers.
 Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
  Output : [[-10, 2, 8], [-7, -3, 10]] 
'''

class TrippleSum:
    def sum_to_zero(self,listt,target):
        l=[]
        for i in range(len(listt)-2):
            for j in range(i+1,len(listt)-1):
                for k in range(j+1,len(listt)):
                    if listt[i]+listt[j]+listt[k]==target:
                        l.append([listt[i],listt[j],listt[k]])
        return l

three_element=TrippleSum()
l=[-25, -10, -7, -3, 2, 4, 8, 10]
target=0
print(three_element.sum_to_zero(l,target))

