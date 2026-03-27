#file handling 
import os
print(os.getcwd())
import numpy as np
arr = np.array([1,2,3,37,13,45])
np.save("num.npy",arr)
retrieve =np.load("num.npy")
print(retrieve)
