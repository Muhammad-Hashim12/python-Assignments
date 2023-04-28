'''
This is problem to convert all the negative coordinates to a positive coordinates;
The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
We can add or delete any number from the coordinates ; however graph should not be changed;

Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]
'''

def cordinate(user_inp,l1=[],l2=[],l=[]):
    for i in user_inp:
        l1.append(i[0])
        l2.append(i[1])
    x_small=abs(min(l1))
    for i,j in zip(l1,l2):
        l.append((i+x_small,j+x_small))
    return l
        

user_inp=[(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]

print(cordinate(user_inp))


