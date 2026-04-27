import pandas as pd

data = {
    "Name": ["Mr_First", "Maker", "Sun"],
    "Age": [16, 16, 15]
}

#df =Data frame it just like 2D array
df = pd.DataFrame(data= data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df)

# Access singular data
print(df.loc["Employee 1"])

# Access with int position
print(df.iloc[1])


# Add new column
df["Job"] = ["N/A", "N/A", "N/A"]
print(df)


# Add new row
new_row = pd.DataFrame([{"Name": "Mint", "Age": 21, "Job": "Reader"}])
# pd.concat([existdataframe, new row])
df = pd.concat([df, new_row])
# Employee 1  Mr_First   16     N/A
# Employee 2     Maker   16     N/A
# Employee 3       Sun   15     N/A
# 0               Mint   21  Reader

# Add label with passing index argument
new_row = pd.DataFrame([
    {"Name": "Fire", "Age": 22, "Job": "Sciantist"}
], index= ["Employee 5"])

df = pd.concat([df, new_row])


# You can also add more than one row
new_rows = pd.DataFrame([
    {"Name": "A", "Age": -1, "Job": "N/A"},
    {"Name": "B", "Age": -1, "Job": "N/A"},
], index=["Employee 6", "Employee 7"])

df = pd.concat([df, new_rows])

print(df)