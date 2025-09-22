import pandas as pd

df = pd.read_csv('./data/stock-data.csv')

df['new_Date'] = pd.to_datetime(df['Date'])
print(df.head())
print()
df.info()

df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
# df['Quarter'] = df['new_Date'].dt.quarter
# df['DayName'] = df['new_Date'].dt.day_name()
# df['M_days'] = df['new_Date'].dt.days_in_month
# df['Hour'] = df['new_Date'].dt.hour
print(df.head()) # hour, minute, second...

# Timestamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_yr'] = df['new_Date'].dt.to_period(freq='Y')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())
print()

# 2018년 6월 데이터만 추출 (문자열 속성 활용)
df_june = df[df['Date_m'].astype(str).str.fullmatch('2018-06')]
print(df_june.head())
print()

# 2018년 6월 데이터만 추출 (Period 객체 활용)
df_june2 = df[df['Date_m'] == pd.Period('2018-06')]
print(df_june2.head())
print()

# df_june2 에서  Date_m 을 인덱스로 지정
df_june2 = df_june2.set_index('Date_m')
print(df_june2.head())
