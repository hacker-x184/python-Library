import numpy as np
# Multi-dimensional arrays
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2D)
print(np.sum(arr2D)) 
sum_of_columns = np.sum(arr2D, axis = 0)
print(sum_of_columns)
sum_of_rows = np.sum(arr2D, axis = 1)
print(sum_of_rows)
print(arr2D[0:2, 1:2])