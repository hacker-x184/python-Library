import numpy as np

#create - from lists
arr = np.array( [1, 2, 3, 4, 5])
print(arr, type(arr), arr.shape)

arr2 = np.array([1, 2, 3, 4, 5, "prime"])
print(arr2, type(arr2), arr2.shape)
#Some sortcut of createing arry
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d, type(arr_2d), arr_2d.shape)
#Prefill array creating trick
arr1 = np.zeros((2,3), dtype="int64")#Filled with zeros
print(arr1)
arr2 = np.ones((2,3), dtype="int64")#Filled with ones
print(arr2)
arr1 = np.full((2,3),50, dtype="int64")#Filled with any value
print(arr1)
arr4 =  np.eye(4)
print(arr4)
arr5 = np.arange(0,11,2) #range
print(arr5,arr5.shape)
arr6 = np.linspace(0,200,5)#Evenly space arraay
print(arr6)
# Properties
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr.ndim)

float_arr = arr.astype(np.float64)
print(float_arr, float_arr.dtype)

