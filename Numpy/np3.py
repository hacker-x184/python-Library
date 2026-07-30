import numpy as np
#Operations on arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr, arr.shape)

reshaped = arr.reshape((3, 2))
print(reshaped, reshaped.shape)

flattened = arr.flatten() # 2D => 1D
print(flattened, flattened.shape)