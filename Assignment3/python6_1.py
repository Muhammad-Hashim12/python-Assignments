'''Write a Python script to sort (ascending and descending) a dictionary by value.'''

fruit_quantity={'apple':5,'kiwi':1,'mango':8,'Lemon':2,'Pear':10,'Atlantic giant pumpkin':1}


if __name__ == '__main__' :
    def asc_sort(fruit):
        return sorted(fruit_quantity.items(),key= lambda x:x[1])
    print(asc_sort(fruit_quantity))

    def desc_sort(fruit):
        return sorted(fruit_quantity.items(),key= lambda x:x[1],reverse=True)
    print(desc_sort(fruit_quantity))