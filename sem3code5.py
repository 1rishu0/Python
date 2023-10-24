''' Design a Python Program to generate and Print a list expect for the first 5 elements, where the values are the squares of numbers between 1 and 30. '''
'''
list1=[1,2,3,4,5]
list2=[]

for i in range (6,31):
    c=i**2
    list2.append(c)
print(list1+list2)
'''

def printvalues():
    list=[]
    for i in range(1,31):
        c=i**2
        list.append(c)
    print(list[5:])
printvalues()
