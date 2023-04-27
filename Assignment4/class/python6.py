''' Write a Python class to implement pow(x, n)'''

class UsePow():
    def implemet_pow(self,val,power):
        return pow(val,power)
    

power_function=UsePow()
val=int(input('enter the number: '))
power=int(input('enter the power number: '))

print(power_function.implemet_pow(val, power))
