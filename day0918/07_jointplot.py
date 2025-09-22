import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

# 디폴트값 = 산점도 (scatter)
j1 = sns.jointplot(x='fare', y='age', data=titanic)
# reg = 회귀선
j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic)
# hex = 육각형
j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic)
# kde = 커널밀도 추정
j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic)

plt.show()