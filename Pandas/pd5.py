import pandas as pd
#CSV DATA 
df = pd.read_csv("employee_data.csv")
print(df , type(df))

#JSON DATA
df1 = pd.read_json("employee_data.json")
print(df1,type(df1))

