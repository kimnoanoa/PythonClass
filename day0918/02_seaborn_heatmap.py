import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

sns.set_style('darkgrid')

table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size', observed=False)
print(table)
table.info()

sns.heatmap(table, annot=True, fmt='d', cmap='YlGnBu', linewidth=.5, cbar=True)
plt.show()