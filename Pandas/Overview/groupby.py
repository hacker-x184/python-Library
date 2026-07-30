import numpy as np
import pandas as pd

data = {
'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
'Store': ['S1', 'S1', '52', 'S2', '51', '52', '52', 'S1'],
'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)
print(df)

#Group by category and calculation

cat = df.groupby('Category')['Sales'].sum()
print(cat)
str = df.groupby('Store')['Sales'].sum()
print(str)

multi = df.groupby(['Category','Store'])['Sales'].sum()
print(multi)

#Aggregation

print(df['Sales'].mean())
print(df['Sales'].median())
"""Meand median mode min max"""
print (df['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median']))