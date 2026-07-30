import numpy as np
# Q16
arr = np.array([[1,2,3],[4,5,6]])
new_arr = np.pad(arr, pad_width = 1,mode = 'constant')
print(new_arr)
# Q17
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 *0.1)
#Q18
matrix = np.zeros((5,5),dtype=int)
for i in range(0,5):
    matrix[i][i-1]=i

print(matrix) 
# Q19
checkboard = np.zeros((8,8),dtype=int)
checkboard[::2,0::2] = 1
checkboard[1::2,1::2] = 1
print(checkboard)
