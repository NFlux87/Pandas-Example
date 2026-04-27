import pandas as pd

# import from csv file
df = pd.read_csv(filepath_or_buffer= 'data/pokemons.csv')

# # default will print 5 first data and last 5 data
# print(df)

# to_sting make it print all data
# if you're looking for column only you can you
# df['column_name']
# df.loc['row_name']
print(df.to_string())
