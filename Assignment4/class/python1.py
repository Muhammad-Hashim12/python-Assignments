'''Write a python class to convert an integer into a roman numeral and viceversa'''


class Convert:
    def to_roman(self,num,val,syb):
        roman_num=''
        i=0
        while num>0:
            for j in range((num//val[i])):
                roman_num+=syb[i]
                num-=val[i]
            i+=1
        return roman_num
    
    def to_int(self,roman,rom_val):
        int_val=0
        for i in range(len(roman)):
            if i>0 and rom_val[roman[i]] > rom_val[roman[i-1]]:
                int_val+=rom_val[roman[i]] -2* rom_val[roman[i-1]]
            else:
                int_val+=rom_val[roman[i]]
        return int_val
                
int_to_roman=Convert()
num=int(input('enter the number: '))
roman=input('enter the roman number: ').upper()
val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]

rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

print(int_to_roman.to_roman(num,val,syb))
print(int_to_roman.to_int(roman, rom_val))







