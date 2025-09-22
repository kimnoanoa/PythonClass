import seaborn as sns
import pandas as pd

# 열 순서 바꾸기

# titanic 데이터셋 로드 및 'survived' : 'age' ==> df 생성!
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, 'survived':'age']

print(df.head())
print()

# 열 이름의 리스트 만들기
print(df.columns)
print(df.columns.to_list())
print(list(df.columns))
print(df.columns.values) # 넘피 배열
columns = list(df.columns.values)
print(columns)

# 알파벳 순으로 정렬하기
columns_sorted = sorted(columns, reverse=False)
print(columns_sorted)
print()

df_sorted = df[columns_sorted]
print(df_sorted.head())
print()

# 알파벳 역순으로 정렬하기
columns_reversed = sorted(columns, reverse=True)
df_reversed = df[columns_reversed]
print(df_reversed.head())
print()

# 수동으로 배치하기
# 원하는 컬럼만 선택이므로, drop의 효과도 같이 볼 수 있음
# reindex 와 비교하여 볼 필요가 있다.
df = df[['pclass', 'age', 'survived', 'sex']]
print(df)
print()