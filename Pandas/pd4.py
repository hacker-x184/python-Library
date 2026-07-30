import pandas as pd
import numpy as np
#Dataframes are the 2d labeled array
info ={
    "Name" : ["Rahul","Rohan","Aniya","Horimiya"],
    "Age" : [18,19,17,16],
    "GPA" : [7.6,8.4,9.2,9.9]
}
df = pd.DataFrame(info)
print(df)
print(df, type(df))
print(df.index)
print(df.columns)

df1 =  pd.DataFrame([["Zoro",19],["Sanji",18],["Copper",15],["Luffy", 15]],index=["King_OF_HEll","BLACK_LEG","COTTON_CANDY","PRIRATES_KING"],columns=["Name","Age"])
print(df1)
np_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
df2 = pd.DataFrame(np_arr,columns=['A','B','C'])
print(df2)
