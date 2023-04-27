'''Write a Python class to find validity of a string of parentheses,
 '(', ')', '{', '}', '[' and ']'. 
 These brackets must be close in the correct order, 
 for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 
 '''

class ParenthesesValidator:
    
    # def __init__(self, input_string):
    #     self.input_string = input_string
    
    def is_valid(self,input_string):
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']' }
        for char in input_string:
            if char in pairs.keys():
                stack.append(char)
            elif char in pairs.values():
                if not stack:
                    return False
                elif pairs[stack.pop()] != char:
                    return False
        return len(stack) == 0

validation=ParenthesesValidator()
ch=input('enter character: ')

print(validation.is_valid(ch))

# input_string = "[)"
# validator = ParenthesesValidator(input_string)
# print(validator.is_valid())  # Output: False
            

