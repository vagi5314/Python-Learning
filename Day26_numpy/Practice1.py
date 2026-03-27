#filtering
import numpy as np
marks = np.array([56,79,23,51,47,89,90,72,66,78,68])
even =marks[(marks%2==0) & (marks>=40)]
are = marks[(marks>=40) | (marks%2==0)]
print(marks>30)
print(even)
print(are)