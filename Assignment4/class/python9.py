'''Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. '''
import math
class Circle:

    def area(self):
        self.radius=int(input('enter the radius of the circle: '))
        self.a=math.pi*self.radius*self.radius
        print(f'The Area of Circle of radius {self.radius} is {self.a:.2f}')

    def perimeter(self):
        self.p=2*math.pi*self.radius
        print(f'The Perimeter of the Circle of radius {self.radius} is {self.p:.2f}')
    
radius_circle=Circle()

radius_circle.area()
radius_circle.perimeter()

