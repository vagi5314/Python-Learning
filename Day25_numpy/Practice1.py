#exercise
import numpy as np
arr = np.array([[1,2,3,4],
[3,7,9,0]], dtype=np.int16)
print(arr)
print(arr.ndim)
print(arr.size)
arr = arr.reshape(4,2)
print(arr)
print(arr.dtype)
