import pandas as pd

# 시리즈 = 인덱스와 데이터

print()
print("----- 리스트를 시리즈로 ----- ")

list_data = ['a',2,'b']
sr = pd.Series(list_data)

print(sr)
print(sr.index)
print(sr.values)
print(type(sr)) # 넘피 기반 구조인 판다스는 데이터 전체를 object 로 가진다.
print(sr.dtype)
print(len(sr))
print(sr.shape)
print(sr.ndim) # 몇차원 ?

print()
print("-----튜플을 시리즈로-----")

tup_data = ('영민','남',True)
sr2 = pd.Series(tup_data,index=['이름','성별','학생여부'])
print(sr2)
print(sr2[0])
print(sr2['이름'])
print(sr2[[1,2]])
print(sr2[1:2])
print(sr2[0:2])
print(sr.index)

print()
print("----- 시리즈 생성 ----- ")

print(pd.Series()) # Series([], dtype: object)

print(pd.Series(5)) # 0    5

print(pd.Series(5,index=['a','b','c'])) 
# a    5
# b    5
# c    5


