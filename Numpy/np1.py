import numpy as np
import time
arr = np.array([1,4,2,5,7])
print(arr)
#execution performance
size = 10_000_000

#python list
py_list = list(range(size))
start = time.time()
sq_list =[x**2 for x in py_list]
end =time.time()
print(f"python list time = {end-start} seconds")

#numpy arrays
np_arr = np.array(py_list)
start = time.time()
sq_array = np_arr**2
end = time .time()
print(f"numpy array time = {end-start} seconds")
