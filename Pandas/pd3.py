import pandas as pd
#Series are Homogenus Only One Type of data and stored on it
#Ther are work on the vectorised system
#Let us examples 
s1 = pd.Series([1,2,3,4,5,6])
s2 = pd.Series([10,20,30,40,50,60])
print(s1+s2)
#They are able to measing valuse as NaN
#iT is the mutable data type but not able to change the size
s1[0] = 100
changed_s1 = s1.drop([0])
print(s1)
print(changed_s1)