# filtering in multidimensional array
import numpy as np
arr =np.array([[2,4,6,8],
[3,7,9,11],
[1,3,5,7]
])
print(arr[(arr%2==0) & (arr>2)])
even = np.where((arr%2==0) & (arr>2), arr, 1)
print(even)
