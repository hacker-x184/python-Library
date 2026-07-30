import numpy as np
#Q6
ar = np.zeros((10),dtype=int)
ar[4]= 1
print(ar)
#Q7
ar1=np.arange(10,50)
print(ar1)
#Q8
print(ar1[::-1])
#Q9
ar_3d = np.arange(9).reshape((3,3))
print(ar_3d)
#Q10
ar3 = np.array([1,2,0,0,4,0])
print(np.where(ar3 != 0))