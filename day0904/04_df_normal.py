import pandas as pd

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

print("---------- 단위 환산 ----------")
print()

print(df.head(3))
print()

# mpg(mile per gallon)  kpl(kilometer per liter) 
# 1 마일 = 1.61km     1갤런 = 3.79 리터
mpg_to_kpl = 1.61 / 3.79

# kpl 열 추가
df['kpl'] = df['mpg'] * mpg_to_kpl

print(df.head(3))
print()

df['kpl'] = df['kpl'].round(2)

print(df.head(3))
print()

print("---------- 자료형 변환 ----------")
print()

# 각 열의 자료형 확인
print(df.dtypes)
print()
df.info()
print()

# horsepower 열의 고윳값 확인
print(df['horsepower'].unique())
print()

# 누락 데이터('?') 삭제
import numpy as np

df['horsepower'] = df['horsepower'].replace('?', np.nan)
df = df.dropna(subset=['horsepower'], axis=0)
df['horsepower'] = df['horsepower'].astype('float')

df.info()
print()
print(df['horsepower'].dtypes)
print()

#---------------------------------------------------

# origin 컬럼 고윳값 확인
print(df['origin'].unique())

# 정수형 데이터를 문자형 데이터로 변환
df['origin'] = df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'})

print(df['origin'].unique())
print()
df.info()
print()
print(df.dtypes)
print()
print('origin 컬럼 데이터 타입:', df['origin'].dtypes)
print()
print(df)

#---------------------------------------------------

# object -- 행마다 문자열 전체를 저장 -- 메모리 낭비.
# category -- 내부적으로 정수 코드로 저장하고, 실제 값은 별도로 보관.
# 연산 속도 향상 / 순서가 있는 범주 표현 가능
df['origin'] = df['origin'].astype('category')
print(df.dtypes)
print()


#---------------------------------------------------

print(df['model year'].sample(3))
print()
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
print()


