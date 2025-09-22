import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)

df = pd.read_csv("./data/auto-mpg.csv",header=None)

# 열 이름 저장
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year', 'origin','name']

# 연비, 실린더수 , 배기량, 마력, 차무게, 가속도, 출시연도, 제조국코드, 차이름
print()
print(df.head())
print()
print(df.tail())
print()
print(df.shape)
print()
df.info()
print()
print(df.dtypes)
print()
print(df['mpg'].dtypes)

# -----------산술정보--------------

print(df.describe()) # 산술정보
print()
print(df.describe(include='all'))






