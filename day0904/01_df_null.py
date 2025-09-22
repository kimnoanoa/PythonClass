import seaborn as sns
import pandas as pd

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

df = sns.load_dataset('titanic')

print(df.head(20))
print()

df.info()
print()

print("---------- 누락 데이터 확인 ----------")
print()

# deck 열의 NaN 개수 계산하기
print(df['deck'].value_counts(dropna=False))
print()

# isnull() 메서드로 누락 데이터 찾기
print(df.head().isnull())
print()

# notnull() 메서드
print(df.head().notnull())
print()

# isnull() 메서드로 누락 데이터 개수 구하기
print(df.isnull().sum(axis=0))
print()

import missingno as msno
import matplotlib.pyplot as plt

# 매트릭스 그래프
msno.matrix(df)
# plt.show()

# 막대 그래프
msno.bar(df)
# plt.show()

# 히트맵 (누락 데이터 변수간 상관관계)
msno.heatmap(df)
# plt.show()

# 덴드로그램
msno.dendrogram(df)
# plt.show()

### ---------- 누락 데이터 표현 ----------

# 기존 방식 (np.nan): 정수형 자료가 float로 변환됨
ser1 = pd.Series([1, 2, None])
print(ser1)

# 정수형이 그대로 유지됨. (결측치는 pd.NA 로 표현)
ser2 = pd.Series([1, 2, None], dtype='Int64')
print(ser2)
