#numpy reshape recap
import numpy as np
arr = np.array([[67,89,34,56,78],
            [34,67,17,39,31]])
print(arr.shape)
print(arr)
arr = arr.reshape(5,2)
print(arr.shape)
print(arr)
arr = arr.reshape(2,-1)
print(arr)
arr = arr.reshape(-1,5)
print(arr)
arr = arr.reshape(10, -1)
print(arr)
