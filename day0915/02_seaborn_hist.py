import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

fig, axes = plt.subplot_mosaic([['top_left','top_right'],
                                 ['middle_left','middle_right'],
                                 ['bottom','bottom']],
                                figsize=(15,6),
                                constrained_layout=True)

sns.histplot(x='age',data=titanic,bins=10,ax=axes['top_left'])
sns.histplot(x='age',hue='survived',data=titanic,ax=axes['top_right'])
sns.histplot(x='age',hue='survived',multiple='dodge', # dodge, stack, layer
             data=titanic, palette='muted', ax=axes['middle_left'])
sns.histplot(x='age', hue='survived',multiple='stack',data=titanic,ax=axes['middle_right'])
sns.histplot(x='age', hue='survived',multiple='fill',bins=10, data=titanic,ax=axes['bottom'])

fig.suptitle('Titanic - Age Distribution')

plt.show()

axes['top_left'].set_title('Histogram')
axes['top_right'].set_title('Histogram(hue)')
axes['middle_left'].set_title('Histogram(multiple - dodge)')
axes['middle_right'].set_title('Histogram(multiple - stack)')
axes['bottom'].set_title('Histogram(multiple - fill)')

plt.show()