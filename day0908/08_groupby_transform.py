import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]

print(df)
print()

# class 로 그룹바이
grouped = df.groupby(['class'],observed=True)

# fare 열을 그룹별로 누적 합산
print(grouped['fare'].cumsum())
print()

print(grouped['fare'].sum())
print()

df['fare_cumsum'] = grouped['fare'].cumsum()
print(df.head())
print()

# transform 에 누적함수 적용
print(grouped[['fare']].transform('cumsum'))
print()

# transform 에 집계함수 사용
print(grouped[['age','survived']].transform('mean'))
print()

# 원본에 바로 붙여주기
df[['age_mean','survived_mean']] = grouped[['age','survived']].transform('mean')
print(df.head())
print()

# z-score 를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

# transform 에 함수 적용
age_zscore = grouped['age'].transform(z_score)
print(age_zscore)
print()

# z-score 를 람다로 적용
# lambda 파라미터 : 변환값
age_zscore2 = grouped['age'].transform(lambda x : (x - x.mean()) / x.std())
print(age_zscore2)
print()

# 내장 집계 함수를 사용하여 반환
age_zscore3 = (df['age'] - grouped['age'].transform('mean')) / grouped['age'].transform('std')
print(age_zscore3)
print()



