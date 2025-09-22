import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',300)

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]
print(df.head())
print()

df2 = pd.pivot_table(df,               # 피벗할 데이터프레임
                      index='class',    # 행 위치에 들어갈 열
                      columns='sex',    # 열 위치에 들어갈 열
                      values='age',     # 데이터로 사용할 열
                      aggfunc='mean',   # 데이터 집계 함수
                      observed=True)

print(df2)
print()

# stack 적용
df_stacked = df2.stack()
print(df_stacked)
print()

# unstack 적용 - level 지정
df_unstacked2 = df2.unstack(level=0)
print(df_unstacked2)
print()

# stack 적용 - level 지정
df_stacked2 = df_unstacked2.stack(level=1,future_stack=True)
print(df_stacked2)
print()


