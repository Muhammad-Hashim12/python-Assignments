'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
'''
total_class=87
class_attend=int(input('total class student attended '))
total_perc=(class_attend/87)*100
print(f'Total calsses attend in percentage {total_perc}% ')
if total_perc>=75:
    print('student is allowed to sit in exam')
else:
    print('student is not allowed to sit in exam.')