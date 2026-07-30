import pandas as pd 
df = pd.read_csv("raw_data.csv")
print(df)
print(df.isnull())
print(df.isna())
print(df.isnull().sum())
print(df.dropna())#Row Drop
print(df.dropna(axis=1))#Column Drop
print(df.fillna(0))
age_mean = df["age"].mean()
df["age"].fillna(age_mean)
print(age_mean)