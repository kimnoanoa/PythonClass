import seaborn as sns
import pandas as pd

# pipe 

titanic = sns.load_dataset('titanic')
df1 = titanic.loc[:, ['age', 'fare']]
df2 = titanic.loc[:, ['embark_town', 'embarked']]


# 각 열의 NaN 찾기
def missing_value(df):
    return df.isnull()

result_df = df1.pipe(missing_value)
print(result_df)
print()

# 각 열의 NaN 개수 반환
def missing_count(df):
    return missing_value(df).sum()

result_series = df1.pipe(missing_count)
print(result_series)
print()

def total_number_missing(df):
    return missing_count(df).sum()

result_value = df1.pipe(total_number_missing)
print(result_value)
print()

# 위 3단계 과정 -- 이렇게 한 것과 같음.
def total_missing(df):
    return df.isnull().sum().sum()

result_value2 = df1.pipe(total_missing)
print(result_value2)
print()

# chain method - 함수 활용
def extract_initial(df):
    df['town_initial'] = df['embark_town'].str[0]
    return df

def verify_initial(df):
    df['verified'] = df['embarked'] == df['town_initial']
    return df

print(df2)
print()

print(verify_initial(extract_initial(df2)))
print()

df2.pipe(extract_initial).pipe(verify_initial)
print(df2)

# 미션
print(df2['verified'].value_counts())
print(df2[df2['verified'] == False])