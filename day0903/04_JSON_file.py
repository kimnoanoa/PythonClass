import pandas as pd
df = pd.read_json('./data/read_json_sample.json')

print(df)
print()

print(df.index)
print()

df2 = pd.read_json('./data/read_json_sample.json',orient='index')
print(df2)