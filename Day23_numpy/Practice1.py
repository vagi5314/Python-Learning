#recaping numpy
import numpy as np
array = np.array([5,6,7,9,0], dtype =np.float16)
print(array)
print(array.dtype)
print(array.size)
print(array.shape)
print(array.ndim)

#type casting
array = array.astype(np.int16)
print(array.dtype)
print(array)