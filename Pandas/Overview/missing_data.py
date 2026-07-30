import numpy as np
import pandas as pd


data = {
'A': [1, 2, np.nan, 4, 5],
'B': [np.nan, 2, 3, 4, 5],
'C': [1, 2, 3, np.nan, np.nan],
'D': [1, np.nan, np.nan, np.nan, 5]
}

df = pd.DataFrame(data)
print(df)
print(df.isna())

print(df.isna().sum())
print(df.isna().any())

print(df.dropna())
print(df.dropna(thresh=2))
print(df.dropna(thresh=3))
print(df.dropna(thresh=1))
print(df.fillna(0))
values = {'A':100,'B':200,'C':300,'D':400}
print(df.fillna(value=values))
print(df.fillna(df.mean()))