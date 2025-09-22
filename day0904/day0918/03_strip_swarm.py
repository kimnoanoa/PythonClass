import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

sns.stripplot(x='class',
              y='age',
              data=titanic,
              ax=axes[0])

sns.swarmplot(x='class',
              y='age',
              data=titanic,
              ax=axes[1],
              hue='class',
              size=4)

axes[0].set_title('Strip Plot')
axes[1].set_title('Swarm Plot')

plt.show()