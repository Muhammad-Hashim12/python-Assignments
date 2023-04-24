'''Write a Python program to extend a list without append.
Sample data: [10, 20, 30]
[40, 50, 60]
Expected output : [40, 50, 60, 10, 20, 30]'''

sample_data1 = [10, 20, 30]
sample_data2 = [40, 50, 60]

def extend(sample_data1,sample_data2):
    for value in sample_data1:
        sample_data2+=[value]
    return sample_data2
print(extend(sample_data1,sample_data2))

#Aother Method

'''sample_data2.extend(sample_data1)
print(sample_data2)'''