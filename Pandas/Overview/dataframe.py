import numpy as np
import pandas as  pd

data = {
'Name': ['John', 'Anna', 'Peter', 'Linda'],
'Age': [28, 34, 29, 42],
'City': ['New York', 'Paris', 'Berlin', 'London'],
'Slalary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)
labels = [1,2,3,4]
data_list = [
['John', 28, 'New York', 65000],
['Anna', 34, 'Paris', 70000],
['Peter', 29, 'Berlin', 62000],
['Linda', 42, 'London', 85000]
]
colums = ['Name','Age','City','Slalary']
dfs = pd.DataFrame(data_list,labels,colums)
print(dfs)


#Selection and Indexing of Columns
print(dfs['Name'])
print(dfs[['Name','City']])

#creating a new Column
dfs['Designation'] = ['Doctor',"Eng.",'Doctor',"Eng." ]
print(dfs)
#Removing a Colum from Dataframes
print(dfs.drop('Designaztion',axis=1))

dfs.drop('Designation',axis=1, inplace = True)
print("New Value")
print(dfs)

#Selecting the row

print(dfs.loc[[1]])
print(dfs.iloc[[1]])
# selecting subset of row and column
print(dfs.loc[[2,3]][['Name','Age']])

#Conditional Selection


#I only want to see those people whose age is above 30

print(dfs[dfs['Age']>30])
#I only want poeple whose age is above 30 and their city must be paris
print(dfs[(dfs['Age'] > 30) & (dfs['City'] == 'Paris')])