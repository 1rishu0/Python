#Pyhton code to perform Arithmetic
# Operations on NumPy array

import numpy as np

# Initialising the array
arr1=np.arange(4,dtype=np.float_).reshape(2,2)

print("First Array:")
print(arr1)

print("\n Second Array:")
arr2=np.array([12,12])
print(arr2)

print("\n Adding the two arrays:")
print(np.add(arr1,arr2))

print("\n Substract the two arrays:")
print(np.subtract(arr1,arr2))

print("\n Multipling the two arrays:")
print(np.multiply(arr1,arr2))

print("\n Division the two arrays:")
print(np.divide(arr1,arr2))
