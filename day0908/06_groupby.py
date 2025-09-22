import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','sex','class','fare','survived']]

print(df.head())
print()

# class 열을 기준으로 그룹화
grouped = df.groupby(['class'],observed=True) #카테고리형 데이터에서 실제로 관측된 조합만 그룹으로 사용하겠다는 의미
print(grouped)
print()

for key,group in grouped:
    print('key : ',key)
    print('number : ',len(group))
    print(group.head())
    print()
    
print()

# 연산 메서드 적용
average = grouped.mean(numeric_only=True) # 계산할 수 있는 숫자 컬럼만
print(average)
print()

group3 = grouped.get_group(('Third',))
print(group3.head())
print()
    
group_two = df.groupby(['class','sex',],observed=True)

for key,group in group_two:
    print('key : ',key)
    print('number : ',len(group))
    print(group.head())
    print()
    
print()

# group_two 에 연산 메서드 적용
average_two = group_two.mean(numeric_only=True)
print(average_two)
print()

# groupby 로 'Third' ,'Female' 만 뽑기
group3f = group_two.get_group(('Third','female'))
print(group3f.head())
print()

# 필터링으로 'Third' ,'female'만 뽑기
group3f = df[ (df['class'] == 'Third') & df(['sex'] == 'female')]
print(group3f.head())
print()



