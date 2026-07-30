import numpy as np
# Q11
arr = np.eye(3,dtype=int)
print(arr)
# Q12
arr1 = np.random.rand(3,3,3)

print(arr1)
#Q13
arr2 = np.random.randint(0,50, (10,10))
print(arr2)
print(np.min(arr2))
print(np.max(arr2))
#Q14
arr3 = np.random.randint(23,657, (3,10))
print(arr3)
print(np.mean(arr3))
#Q15
num = int(input("Enter the number that you want to create the matrix:--"))
arr4 = np.ones((num,num),dtype=int)
arr4[1:-1 ,1:-1] = 0
print(arr4)