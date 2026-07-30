import numpy as np
import pandas as pd

labels = [1,2,3]
my_list = [10,20,30]
arr = np.array([10,20,30])
d = { 1:10,2:20,3:30}
print(pd.Series(labels))
print(pd.Series(my_list))
print(pd.Series(arr,labels))
print(pd.Series(d))