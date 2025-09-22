import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
df = df.drop(columns=['Date'])
df = df.set_index('new_Date').sort_index()

ts = df.head(10)
print(ts)
print()

#-----------------------------------------------

print(ts.shift(1))
print()
print(ts.shift(-2))
print()

print(ts.shift(3, freq="D"))
print()

print(ts.asfreq('5D'))
print()

print(ts.asfreq('5D', method='bfill'))
print()

# Resampling
print(ts.resample('3B'))
print()

print(ts.resample("3B").sum())
print(ts.resample("3B").mean())
print(ts.resample("3B").median())
# min, max, count...

print(ts.rolling(window=3).sum())
print()
print(ts.rolling(window='3D').sum())
print()