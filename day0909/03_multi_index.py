import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]
print(df)
print()

grouped = df.groupby(['class','sex'],observed=True)
gdf = grouped.agg(['mean','std'], numeric_only = True)
print(gdf)
print()

print(gdf.index)
print()

# 멀티 인덱스 만들기 - 배열의 인덱스를 이용
arrays = [['a','a','b','b'],[1,2,1,2]]
multi_index_arrays = pd.MultiIndex.from_arrays(arrays, names=('letter','number'))
print(multi_index_arrays)
print()

# 멀티 인덱스 만들기 - 튜플의 배열을 이용
tuples =[('a',1),('a',2),('b',1),('b',2)]
multi_index_tuples = pd.MultiIndex.from_tuples(tuples, names=('letter','number'))
print(multi_index_tuples)
print()

# 멀티 인덱스 만들기 - 교차 반복객체를 이용
letters = ['a','b']
numbers = [1,2]
multi_index_product = pd.MultiIndex.from_product([letters,numbers],
                                                 names=('letter','number'))

print(multi_index_product)
print()

# 멀티 인덱스 만들기 - 데이터 프레임을 이용
df = pd.DataFrame([['a',1],['a',2],['b',1],['b',2]],columns = ['letter','number'])
multi_index_frame = pd.MultiIndex.from_frame(df)
print(multi_index_frame)
print()

# 멀티 인덱스의 특정 레벨을 추출 1
print(multi_index_frame.get_level_values(0))
print()

# 멀티 인덱스의 특정 레벨을 추출 1
print(multi_index_frame.get_level_values('letter'))
print()

print(gdf)
print()

# 컬럼의 멀티 인덱스 확인
print(gdf.columns.levels)
print()

# 레벨을 지정하여 열 인덱스 추출
print(gdf.columns.get_level_values(0))
print()

# 레벨을 지정하여 열 인덱스 추출
print(gdf.columns.get_level_values(1))
print()

print(gdf['age'])
print()

print(gdf['age','mean'])
print()

# name : mean
print(gdf['age']['mean'])
print()

# class 값이 first 인 행을 선택
print(gdf.loc['First'])
print()

print(gdf.loc[('First','female')])
print()

print(gdf.loc[('First','female'),('age','mean')])
print()

print(gdf)
print()

# first female 인데 
print(gdf.loc[('First','female'),('age','std'):('fare','std')])
print()

# 특정 레벨에서 교차 섹션 (cross-section) 이용 - sex 값이 male 인 데이터를 선택
male_class = gdf.xs('male',level='sex')
print(male_class)
print()

# 멀티인덱스 정렬
print(gdf.sort_index(level=0, ascending=False))
print()

print(gdf.sort_index(level='sex',ascending=False))
print()

print(gdf.sort_index(level=['sex','class'], ascending=[False,True]))
print()

