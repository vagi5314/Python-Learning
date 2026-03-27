#linear algebra
import numpy as np
arr = np.array([[1,7,3], [9,5,2], [4,6,8]])
brr = np.array([[23,3,7], [9,2,1], [4,5,6]])
print(np.dot(arr, brr))
print(np.linalg.det(arr))
print(np.matmul(arr, brr))
print(arr.T)
print(np.cross(arr, brr))
print(np.linalg.inv(brr))