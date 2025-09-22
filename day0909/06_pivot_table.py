import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',300)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]
print(df.head())
print()

pdf1 = pd.pivot_table(df,               # 피벗할 데이터프레임
                      index='class',    # 행 위치에 들어갈 열
                      columns='sex',    # 열 위치에 들어갈 열
                      values='age',     # 데이터로 사용할 열
                      aggfunc='mean',   # 데이터 집계 함수
                      observed=True)

print(pdf1)
print()

pdf2 = pd.pivot_table(df,               # 피벗할 데이터프레임
                      index='class',    # 행 위치에 들어갈 열
                      columns='sex',    # 열 위치에 들어갈 열
                      values='survived',     # 데이터로 사용할 열
                      aggfunc=['mean','sum'],   # 데이터 집계 함수
                      observed=True)

print(pdf2)
print()

pdf3 = pd.pivot_table(df,               # 피벗할 데이터프레임
                      index=['class','sex'],    # 행 위치에 들어갈 열
                      columns='survived',    # 열 위치에 들어갈 열
                      values=['age','fare'],     # 데이터로 사용할 열
                      aggfunc=['mean','max'],   # 데이터 집계 함수
                      observed=True)

print(pdf3)
print()



