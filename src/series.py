import pandas as pd

# Series =  A Pandas 1-Dimensional labeled array that can hold any data type
#           Think of it like 1 column in a spreadsheet(1 Dimensional)

datas = pd.array([100, 102, 104, 200, 202])           
# index data
# 0     100
# 1     102
# 2     104
# dtype: int64 -> Change on data type
series = pd.Series(data= datas)
print(series)

# Change index label Default [0, 1, 2, ..]
series = pd.Series(data= datas, index= ['a', 'b', 'c', 'd', 'e'])   # index should have same size as  data                    
print(series)


# Acces data in series
# series.loc["label"]
print(series.loc["a"])

series.loc['c'] = 250
print(series.loc['c'])

# Access by int position
print(series.iloc[1])


#filter by value
print(series[series <= 200])


# dictionary will conatin key and value so 
# Key will set to label
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories) # Don't need to pass in index= 

print(series.loc["Day 3"])
series.loc["Day 3"] += 500

print(series.loc["Day 3"])


print(series[series <= 2000])