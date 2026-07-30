import numpy as np
#3D array
arr3D = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
print(arr3D, arr3D.shape)
#indexing
print(arr3D[1, 1, 0])
#slicing
arr3D[:, 0, :] = 99 # ffrst row from both layers
print(arr3D)

#2 x 3 x 2