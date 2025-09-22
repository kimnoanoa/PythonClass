import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])

print(df)
print()

df = df.set_index('new_Date').sort_index()
df = df.drop('Date', axis=1)
print(df)
print()
print(df.index)
print()

# 부분 문자열 인덱싱 1
print(df.loc['2018-06-27'])
print()

# 부분 문자열 인덱싱 2
print(df.loc['2018-07'])
print()

# 부분 문자열 인덱싱 3
print(df.loc['2018-06-27':'2018-07-02'])
print()

# 부분 문자열 인덱싱 4
print(df[df.index < '2018-06-05'])
print()

# 시간 자료형을 활용한 인덱싱1
print(df.loc[pd.Timestamp(2018, 6, 27):pd.Timestamp(2018, 7, 2)])
print()

# 시간 자료형을 활용한 인덱싱2
print(df.loc[pd.Timestamp(2018, 6, 27, 10, 30, 0):pd.Timestamp(2018, 7, 2, 23, 59, 59)])
print()

# --------------------------------------------------------

# 날짜,시간 간격을 표현하는 pandas.Timedelta 객체
print(pd.Timedelta("1 days"))
print(pd.Timedelta(days=1))
print(pd.Timedelta("1 days 1hours 1 minutes 1 seconds"))
print(pd.Timedelta(days=1, hours=1, minutes=1, seconds=1))
print()

print(pd.to_timedelta(['1 days', '3 hours']))
print()

a = df.index
print(a)
print()

b = pd.Timestamp('2018-07-03') - a
print(b)
print()

c = a + pd.Timedelta(days=1)
print(c)
print()

print(c.min())
print(c.max())