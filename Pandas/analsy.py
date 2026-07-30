import pandas as pd
data = pd.read_csv("globalAirQuality.csv")
print(data.head())
print(data.tail())
print(data.sample(6))
print(data.describe())
print(data.shape)
print(data.nunique())