#slicing
import numpy as np
arr = np.array([
    [1,2,3],
    [1,5,7],
    [11,4,9],
    [2,7,9]]
)
print(arr)

print(arr[0:1:,1:3:])

print(arr[0])

print(arr[1:3:,0:3:])

print(arr[0,0])

print(arr[3,:])
