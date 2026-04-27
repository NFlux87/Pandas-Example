import pandas as pd

df = pd.read_csv('data/pokemons.csv')

# Aggregate function = Sumurize data to one data Example - Find Average

# print(df.mean()) # Cannot perform reduction 'mean' with string dtype
# These Aggregate Function will apply to whole data frame
print(df.mean(numeric_only= True))
print(df.sum(numeric_only= True))
print(df.min(numeric_only= True))
print(df.max(numeric_only= True))
print(df.count()) # count won't include any null value

# Single column
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].min())
print(df["Height"].max())
print(df["Type2"].count())


# Group Frame
group = df.groupby("Type1")

# What is average height by group 
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())