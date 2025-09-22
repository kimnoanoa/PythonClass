import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())
print()

sns.set_style('darkgrid')

fig, axes = plt.subplots(1,2,figsize =(15,5))

sns.regplot(x='age',y='fare',data=titanic,ax=axes[0]) # x축은 age, y축은 fare 로 설정 (데이터 타이타닉)
sns.regplot(x='age',y='fare',data=titanic,ax=axes[1] ,fit_reg=False) # 기본적으로 회귀선을 그리는데 회귀선 없애는 옵션
plt.show()

fig, axes = plt.subplots(1,2,figsize =(15,5))
sns.scatterplot(x='age',y='fare',hue='sex', data=titanic ,ax=axes[0]) # hue 를 써두면 범주를 알아서 색상으로 구분해 시각화함
sns.scatterplot(x='age',y='fare',hue='survived', data=titanic ,ax=axes[1])
plt.show()