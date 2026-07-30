import numpy as np
#vectorization

arr1 = np.array( [1, 2, 3, 4, 5])
arr2 = np.array( [6, 7, 8, 9, 10])

print(arr1 + arr2)
#broadcasting

arr3 = np.array( [1, 2, 3, 4, 5])
arr4 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

print(arr3 + arr4)

#normalize

arr5 = np.array( [[1, 2], [3, 4]])

mean = np. mean(arr5)
std_dev = np.std(arr5)

normalized_arr = (arr5-mean)/std_dev
print(normalized_arr)
#Mathematical fnx

#aggregation

arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))
print (np.prod(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr))
print(np.argmax(arr))

print(np.mean(arr))
print(np.std(arr))
print(np.median(arr))
print(np.var(arr))
