import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

# sns.displot(titanic['fare'], kind='hist')
# # plt.show()

# sns.displot(titanic['fare'], kind='kde')
# # plt.show()

sns.displot(data=titanic, x='fare', col='pclass', kind='hist')

sns.displot(data=titanic, x='fare', row='survived', kind='kde', fill=True)
# plt.show()

sns.displot(data=titanic, x='fare', row='survived', col='pclass')
# plt.show()

sns.displot(data=titanic, x='fare', y='age', kind='kde')

sns.displot(data=titanic, x='fare', y='age', kind='kde', fill=True)
# plt.show()

sns.displot(data=titanic, x='fare', y='age', kind='hist')
plt.show()