# 커널 밀도 그래프 (kernel Density Estimate Plot)

import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
sns.set_style('darkgrid')

fig, axes = plt.subplot_mosaic([['top_left','top_center','right'],
                                ['bottom_left','bottom_center','right']],
                               figsize=(15,6),
                               constrained_layout=True)

sns.kdeplot(x='age',data=titanic, ax=axes['top_left'])
sns.kdeplot(x='age',data=titanic,hue='survived', ax=axes['bottom_left'])
sns.kdeplot(x='age',data=titanic,hue='survived', fill=True, ax=axes['top_center'])
sns.kdeplot(x='age',data=titanic,hue='survived', multiple='stack', ax=axes['bottom_center'])
sns.kdeplot(x='age',data=titanic,hue='survived', multiple='fill', bw_adjust=2.0, ax=axes['right'])

plt.show()


