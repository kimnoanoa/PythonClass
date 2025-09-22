import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('ticks')

fig, axes = plt.subplots(2, 2, figsize=(10, 6), constrained_layout=True)


sns.barplot(x='sex', y='survived', data=titanic, ax=axes[0,0])

sns.barplot(x='sex', y='survived', data=titanic, errorbar=None, ax=axes[0,1])

sns.barplot(x='sex', y='survived', data=titanic, 
            hue='class', errorbar=('ci', 95), ax=axes[1,0], estimator='mean')

sns.barplot(x='sex', y='survived', data=titanic, hue='class', dodge=False, ax=axes[1,1])

plt.show()