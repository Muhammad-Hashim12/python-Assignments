'''Write a Python program to check a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with two equal sides.
Expected Output:
Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle '''

x,y,z=6,8,12

if x==y and y==z and x==z:
    print('triangle is equilateral')
elif  x==y or y==z or x==z:
    print('isosceles triangle')
elif x!=y and y!=z and x!=z:
    print('Scalene triangle')
