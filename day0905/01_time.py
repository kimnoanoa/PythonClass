# 시계열 데이터를 용이하게 다루기 위한 시간 자료형
# Timestamp 와 Period
#  (그 시점)   ( 기간 )

import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

print(df)
print()
df.info()
print()

# 문자열 데이터 'Date' 컬럼을 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])

print(df)
print()
df.info()
print()
print(type(df['new_Date'][0]))
print()

# new_Date 를 인덱스로 설정
# Date 컬럼은 삭제
df = df.set_index('new_Date')
df = df.drop('Date', axis=1)

print(df)
print()
df.info()
print()


# DatetimeIndex
# 시계열 데이터의 인덱스로 쓰이기 위해 설계된 자료 구조
print("-----pd.DatetimeIndex-----")
print()
print(pd.DatetimeIndex(["2022-12-25", "2024/02/29", "1999.12.31"]))
print()

# Timestamp
print("-----pd.Timestamp-----")
print()
print(pd.Timestamp("04-30-2012")) # 2012-04-30 00:00:00
print(pd.Timestamp("30-04-2012")) # 2012-04-30 00:00:00
print(pd.Timestamp("04-06-2012")) # 2012-04-06 00:00:00
print()

print("-----pd.to_datetime-----")
print()
print(pd.to_datetime("2023년 12월 25일", format="%Y년 %m월 %d일"))
print(pd.to_datetime("12-12-2025 23:59:12", format="%d-%m-%Y %H:%M:%S"))
print(pd.to_datetime("2023ㅋㅋ 12ㅎㅎ 25??", format="%Yㅋㅋ %mㅎㅎ %d??"))
print()

# Timestamp를 Period로 변환

dates = ['2019-01-01', '2020-03-01', '2021-06-01']

ts_dates = pd.to_datetime(dates)
print(ts_dates)
print()

pr_day = ts_dates.to_period(freq='D')
print(pr_day)
print()
pr_month = ts_dates.to_period(freq='M')
print(pr_month)
print()
pr_year = ts_dates.to_period(freq='Y')
print(pr_year)
print()

