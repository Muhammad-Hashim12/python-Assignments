'''Write a python class which has 2 methods get_string and print_string. 
get_string takes a string from the user 
and print_string prints the string in reverse order
 '''

class Use2Methods:
    def get_string(self):
        self.string=input('enter the character:')


    def print_string(self):
        print('after reversing string: ',self.string[::-1])

two_method=Use2Methods()
two_method.get_string()
two_method.print_string()


