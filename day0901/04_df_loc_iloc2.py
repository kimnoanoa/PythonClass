import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

students = {'수학':[90, 80, 70], '영어':[88, 77, 66], '사회':[30, 40, 50]}
df = pd.DataFrame(students, index=['철수', '영수', '정수'])
print(df)
print()

print("----- 원소 반환 -----")
print()

df2 = df.loc['철수', '수학']
print(type(df2)) # <class 'numpy.int64'> -- 넘피가 제공하는 64비트 정수 자료형
print(df2)

df2 = df.iloc[0,0]
print(df2)
print()

print("----- 시리즈 반환 -----")
print()

# 철수의 수학, 영어 점수 loc, iloc

df3 = df.loc['철수', ['수학', '영어']]
print(df3)
print(type(df3))
print()

df3 = df.iloc[0, [0, 1]]
print(df3)

print("----- 데에터프레임 반환 -----")
print()

df4 = df.loc[['철수', '정수'], ['수학', '영어']]
print(df4)
print(type(df4))
print()

df4 = df.iloc[[0, 2], [0, 1]]
print(df4)

df4 = df.loc['철수':'정수', '수학':'영어']
print(df4)

df4 = df.iloc[0:3, 0:1]
print(df4)