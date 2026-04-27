import pandas as pd

df = pd.read_csv("data\pokemons.csv")

# # Selection by Column

# Print entried thing
# print(df["Name"].to_string())

print(df["Name"])
print(df["Height"])
print(df["Weight"])

# Access Multiple column
# df[[List_name_of_column]]
print(df[["Name", "Height", "Weight"]].to_string())


# Selection By row
print(df.loc[0])
print(df.loc[1])

# You can make label to somthin like name or id
# Set each rows to pokemon name
df = pd.read_csv("data\pokemons.csv", index_col= "Name")

print(df)
# Search by name
print(df.loc["Pikachu"])
# You can also select column you want
print(df.loc["Charizard", ["Height", "Weight"]])

# Select with slice
print(df.loc["Charizard":"Pikachu"])


# Access by int location
print(df.iloc[0:11:2, 0:3])