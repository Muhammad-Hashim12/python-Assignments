'''Write a Python class to reverse a string word by word. 
Input string : 'hello .py' Expected Output : '.py hello' '''

class StringReverse():
    def reverse_str(self,words):
        s=''
        for word in words:
            s+=word+' '
        
        return s
        


reversing_words=StringReverse()
string='hello .py'
words=string.split(' ')
words.reverse()
print(reversing_words.reverse_str(words))



