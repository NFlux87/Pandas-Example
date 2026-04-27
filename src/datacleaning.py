import pandas as pd

# Data Cleaning =   The process of fixing/removing:
#                   incomplete, incorrect, or irrelevant data
#                   ~75% of work done with Pandas is data cleaning

df = pd.read_csv("data/pokemons.csv")

# 1. Drop irrelevent collumn
df = df.drop(columns= [ "No"])

# 2. Handle missing data na = Not Avarible
# Droping value That missing 
# df = df.dropna(subset= ["Type2"])

# instant of droping you can use fill to chang Nan to something
# df.fillna({columnd : Value})
df = df.fillna({"Type2": "None"})


# 3. Fix incosistent values
# df["column"].replace({"from": "to"})
df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
                                   "Fire": "FIRE"})

# 4. Standardsize text

df["Name"] = df["Name"].str.lower()

# 5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove dupicate
df = df.drop_duplicates()

# reset_index
# df = df.reset_index(drop=False)
print(df.to_string())