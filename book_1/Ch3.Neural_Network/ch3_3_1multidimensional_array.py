import numpy as np

A = np.array([[[1, 2, 3, 4], 
             [4, 5, 6, 4], 
             [4, 5, 6, 4]],

             [[0, 5, 6, 4], 
             [11, 5, 6, 4], 
             [4, 5, 6, 4]]])

print(np.ndim(A))
print(A.shape)
print(A.shape[0])