import pandas as pd
s = pd.Series([1,2,3,4,5])
print(s)
print(type(s))

#indexing
print(s[1])
print(s[3])
print(s[0])

labels = ['A','B','C','D','E']
s1 = pd.Series([32,34,54,23,43],index = labels)

print(s1)
s1 = pd.Series([32,34,54,23,43],labels)
print(s1)
print(s1['E'])
print(s1['A'])
print(s1['D'])
print(s1['B'])