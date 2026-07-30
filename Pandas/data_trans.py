import pandas as pd
df = pd.read_csv("raw_data.csv")
df2 = df.copy()

df2["tax"] = df2["income"].apply(lambda x : "20%" if x >= 60000 else "10%")

gender_map = {"Male" : "M", "Female" : "F", "Unknown" : "U"}
df2["gender"] = df2["gender"].map(gender_map)

df2 = df2.assign(new_income =df2["income"] * 1.1)

df2["country"] = df2["country"].replace("USA", "US")
print(df2)
df2.columns = ["Id", "Name", "Age", "Country", "Gender", "Income", "Tax", "New_Income"]
df2. rename(columns={"Income":"Salary"})
df2. rename(index={1:"First"})

df2.sort_values("Income")
df2 = df2.fillna(50)
# df2.sort_values("Income", ascending=False)
sorted_df = df2.sort_values(["Income","Age"])
print(df2)
sorted_df.sort_index()

# reset
sorted_df. reset_index()
sorted_df. reset_index(drop=True)

# Ranking
# sorted_df["Ranking"]= sorted_df["Income"].rank(ascending=False, method="max")
sorted_df[["Id", "Name", "Age", "Country", "Gender", "Income","New_Income", "Tax"]]
print(sorted_df)