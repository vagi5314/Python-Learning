#multidomensional array recap
import numpy as np
one_d = np.array([1,5,6,7,23])
print(one_d)
print(one_d.ndim)
print(one_d[2:4])

two_d = np.array([
    [1,4,5],
    [3,7,9]
])
print(two_d)
print(two_d.ndim)
print(two_d[1,2])
print(two_d[0,:])

three_d = np.array([
    [
        [7,9,3],
        [3,1,7]
    ],
    [
        [1,2,3],
        [4,5,6]
    ]
])
print(three_d)
print(three_d.ndim)
print(three_d[0,1,2])
print(three_d[0,1,:])