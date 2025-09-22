import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

# 엑셀 데이터셋 불러오기

df = pd.read_excel('./data/주가데이터.xlsx')
print(df.head())
print()

df.info()
print()

# 연, 월, 일 데이터 분리하기
df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')

print(dates.head())

# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)

print(df.head())
print()

# expand 옵션

df_expand = df['연월일'].str.split('-', expand=True)
df_expand.columns = ['연', '월', '일']
print(df_expand.head())
print()

# ---------- 타임 스탬프 방법으로 해보기 ----------
df.info()
print()

df['연월일'] = pd.to_datetime(df['연월일'])
df.info()
print()

# 연, 월, 일 바로 추출
df['연'] = df['연월일'].dt.year
df['월'] = df['연월일'].dt.month
df['일'] = df['연월일'].dt.day
df['요일'] = df['연월일'].dt.day_name()

print(df.head())
print()