import seaborn as sns
import pandas as pd

# ---------- 데이터프레임에 map 적용 ----------

# titanic 에서 age, fare 선택하여 df 만들기
titanic = sns.load_dataset('titanic')
df = titanic[['age', 'fare']]
print(df.head())
print()

# 사용자 함수 정의
def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b

# 데이터프레임의 모든 원소를 add_10() 함수에 매핑
df_map = df.map(add_10)
print(df_map.head())
print()

# 람다 함수 활용
df2 = df.map(lambda n: n + 10)
print(df2.head())
print()

# 함수의 매개변수가 2개 이상인 경우
df3 = df.map(add_two_obj, b=10)
print(df3.head())
print()

# 함수의 매개변수가 2개 이상인 경우 (람다 함수 활용)
df4 = df.map(lambda a, b: a + b, b=10)
print(df4.head())
print()


# ---------- 데이터프레임에 apply 적용 (열/행 전달) ----------

# ---------- 열 전달 ----------

def calculate_stats(col):
    max_val = col.max()
    min_val = col.min()
    mean_val = col.mean()
    median_val = col.median()

    return pd.Series([max_val, min_val, mean_val, median_val], index=['Max', 'Min', 'Mean', 'Median'])

# 각 열에 calculate_stats 함수 적용
result_df = df.apply(calculate_stats, axis=0)

print(result_df)
print()

# 각 열에 람다 함수 적용 
result_sr = df.apply(lambda x: x.max() - x.min(), axis=0)

print(result_sr)
print()


# ---------- 행 전달 ----------

# 각 행에 대해 최대값과 최소값의 차이와 평균을 계산하는 함수
def calculate_diff_avg(row):
    diff = row.max() - row.min()
    avg = row.mean()
    # 새로운 시리즈 반환
    return pd.Series([diff, avg], index=['차이', '평균'])

# apply 함수를 사용하여 각 행에 calculate_diff_avg 함수 적용
result_df2 = df.apply(calculate_diff_avg, axis=1)

print(result_df2)
print()


# 람다 함수를 사용하여 각 행에 대해 계산 적용 (multi 매개변수 추가)
result_df3 = df.apply(lambda row, multi: pd.Series([(row.max() - row.min()) * multi, row.mean()], 
                                                   index=['차이', '평균']), multi = 2, axis=1)

print(result_df3)
print()

# 평균값이 30을 초과하는 열만 필터링
filtered_columns = df.apply(lambda x: x.mean() > 30) # axis=0 생략

print(filtered_columns)
print()

filtered_df = df.loc[:, filtered_columns]

print(filtered_df)
print()

# df의 각 행의 평균이 50을 초과하면 'Yes' 아니면 'No'인 컬럼 'High' 만들기 (apply, 람다식 사용)
df['High'] = df.apply(lambda row: 'Yes' if row.mean() > 50 else 'No', axis=1)

print(df)
print()