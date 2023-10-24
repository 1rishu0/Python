# Built in function of numpy

import numpy as np
'''
l=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    num=int(input("Enter the number:"))
    l.append(num)
arr=np.array(l)
print(arr)
print(arr.ndim)
'''

matrix=[]
r=int(input("Enter the number of row:"))
c=int(input("Enter the number of columns:"))
for i in range(r):
    a=[]
    for j in range(c):
        n=int(input("Enter the number:"))
        a.append(n)
    matrix.append(a)
m=np.array(matrix)
print(m)
print(m.ndim)
print(m.shape)
print(m.size)