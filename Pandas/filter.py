import pandas as pd
df = pd.read_csv("globalAirQuality.csv")
print(df[(df["aqi"]>100) & (df["temperature"]>20)]) 
# Filtering of Data

df[ df["aqi"] > 100 ]
df[ (df["aqi"] >100) & (df["temperature"] > 30) ]
df[ (df["aqi"] > 100) & (df["temperature"] < 30) ]

aqi_data = df[ (df["aqi"] >100) & (df["temperature"] > 30) ] [["city", "aqi"]]

print(aqi_data)
print(aqi_data.iloc[0])
print(aqi_data. loc[6])
#Using the Query methods
print(df.query("aqi>100")) 