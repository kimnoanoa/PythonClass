import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)

students = {'이름':['서준', '우현', '인아'],
            '수학':[90, 80, 70], 
            '영어':[88, 77, 66], 
            '사회':[30, 40, 50]}

df = pd.DataFrame(students)
print(df)
print()

df.index=['가', '나', '다']
print(df)
print()

df = df.set_index('이름')
print(df)
print()

print("----- 열 추가하기 -----")
print()

df['국어'] = 80
print(df)
print(df.shape) # (3, 4) 인덱스랑 컬럼 빼고 자료만.
print()

# ------------------------------------------------
from tabulate import tabulate

print(tabulate(df, headers='keys', tablefmt='psql'))
print()
# grid  pipe  fancy_grid  github  psql
# ------------------------------------------------

df['미술'] = [89, 90, 91]
print(df)
print()


print("----- 행 추가하기 -----")
print()

df.loc['동수'] = 0
print(df)
print()

df.loc['말숙'] = [34, 54, 77, 88, 90] # 개수에 맞게 넣기
print(df)
print()

print("----- 원소 값 변경 -----")
print()

df.loc['동수', '수학'] = 65
print(df)
print()

df.iloc[3, 1] = 70
print(df)
print()

df.loc['동수', '사회':'미술'] = [90, 98, 100]
print(df)
print()

df.loc['동수', ['수학', '국어']] = [98, 65]
print(df)
print()

print("----- 행, 열 자리바꾸기 (전치) -----")
print()

df = df.transpose()
print(df)
print()

df = df.T
print(df)
print()




