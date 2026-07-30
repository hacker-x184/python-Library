import pandas as pd
df = pd.read_csv("globalAirQuality.csv")
#Selecting Data
print(df[['city']])
print(df[['city','aqi']])

#Loc Row  index that we want the data
print(df.loc[0])
print(df.loc[0:2])
#iLoc Row  index that we want the data
print(df.iloc[0:2])

# For  the indivisual cell For the Row and column Data
print(df.loc[0:3,['aqi','city']])
print(df.columns)
print(df.iloc[0:3,[2,11,5]])
# Cell
print(df.at[0, "city"])
print(df.iat[0,"2"])