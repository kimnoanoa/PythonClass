import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.max_columns',None)
pd.set_option('display.width',300)                                                                                                                                                                                         

# 주가 데이터
df1 = pd.read_excel('./data/stock_price.xlsx')
print(df1)
print()

# 주식 가치평가 데이터
df2 = pd.read_excel('./data/stock_valuation.xlsx')
print(df2)
print()

# 데이터프레임 합치기 - 교집합
merge_inner = pd.merge(df1,df2,how='inner',on='id')
print(merge_inner)
print()

# 데이터프레임 합치기 - 교집합
merge_inner2 = pd.merge(df1,df2,how='inner',left_on=['id','stock_name'],right_on=['id','name'])
print(merge_inner)
print()

# 데이터프레임 합치기 - 합집합
merge_outer = pd.merge(df1,df2,how='outer',on='id')
print(merge_outer)
print()

# 왼쪽 기준으로 합치기
merge_left = pd.merge(df1,df2,how='left',on='id')
print(merge_left)
print()

# 오른쪽 기준으로 합치기
merge_right = pd.merge(df1,df2,how='right',on='id')
print(merge_right)
print()

# 교차 조인
merge_cross = pd.merge(df1,df2,how='cross')
print(merge_cross)
print()

price = df1[df1['price'] < 50000 ]
print(price)
print()

value = pd.merge(price,df2) # how = inner , on=id 디폴트
print(value)
print()

# 데이터프레임 생성
sdf1 = pd.DataFrame({'employee': ['Alice', 'Sam', 'Eva'],
                    'department': ['HR', 'Tech', 'HR']})
sdf2 = pd.DataFrame({'employee': ['Eva', 'Alice', 'Sam'],
                    'start_year': [2018, 2019, 2020]})

# one-to-one 조인
result_one_to_one = pd.merge(sdf1, sdf2, on='employee')
print(result_one_to_one)
print()

sdf3 = pd.DataFrame({'department':['HR','Tech'],
                     'manager':['Tina','Alex']})

# Many-to-one
result_many_to_one = pd.merge(sdf1,sdf3,on='department')
print(result_many_to_one)
print()

# 데이터프레임 생성
sdf4 = pd.DataFrame({'department': ['HR', 'HR', 'Tech', 'Tech', 'Finance'],
                    'task': ['recruiting', 'payroll', 'development', 'support', 'budgeting']})

# Many-to-Many
result_many_to_many = pd.merge(sdf1, sdf4, on='department')
print(result_many_to_many)
print()

