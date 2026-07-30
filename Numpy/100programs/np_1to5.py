#Q1
import numpy as np
#Q2
np.__version__

print(np.__version__)



#Q3
null_vector = np.zeros((10),dtype=int)
null_vector = np.zeros((1,10),dtype=int)
print(null_vector)
#Q4
print("size of the  array in bytes",null_vector.nbytes)
print("memory size of the  array",null_vector.size * null_vector.itemsize)


#Q5
print(np.add.__doc__)
