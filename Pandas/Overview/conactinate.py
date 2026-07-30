import numpy as np
import pandas as pd
df1 = pd.DataFrame({
'A': ['A0',  'A1', 'A2'],
'B': ['B0', 'B1', 'B2'],
'C': ['CO', 'C1', 'C2']
})
df2 = pd.DataFrame({
'A': ['A3', 'A4', 'A5'],
'B': ['B3', 'B4', 'B5'],
'C': ['C3', 'C4', 'C5']
})
print(df1)
print(df2)
print(pd.concat([df2 ,df1]))
print(pd.concat([df1 ,df2]))
print(pd.concat([df1 ,df2],axis=1))
# Joining  2 data frames 
df1 = pd.DataFrame({
'name': ['Alice', 'Bob', 'Charlie']
}, index=[1, 2, 3])

# Second DataFrame
df2 = pd.DataFrame({
'score': [85, 90, 75]
}, index=[2, 3, 4])
print(df1)
print(df2)

print(df1.join(df2,how='outer'))
print(df2.join(df1,how='outer'))