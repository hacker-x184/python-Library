import numpy as np
#Indexing
arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[2])

#Fancy Indexing
arr2 = np.array([1, 2, 3, 4, 5])
idx = [0, 1, 3]
print(arr2[idx])
#Boolean Indexing
arr3 = np.array([1, 2, 3, 4, 5])

print(arr3[arr3 > 2])
print(arr3[arr3 % 2 == 0])
#Slicing
arr4 = np.array([1, 2, 3, 4, 5])

print(arr4[1:4]) #[start, end, step]
print(arr4[1:])
print(arr4[:4])
print(arr4[::2])