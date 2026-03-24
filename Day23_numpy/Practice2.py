#multidomensional array recap
import numpy as np
one_d = np.array([1,5,6,7,23])
print(one_d)
print(one_d.ndim)

two_d = np.array([
    [1,4,5],
    [3,7,9]
])
print(two_d)
print(two_d.ndim)

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