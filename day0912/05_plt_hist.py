import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic')

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(8,5))
plt.title('Histogram')
plt.xlabel('mpg')
# plt.show()

plt.figure(figsize=(8,5))
plt.hist(df['mpg'],bins=10)
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()

df[['mpg', 'origin']].plot(by=['origin'], kind='hist', figsize=(8,10))
# plt.show()

fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(10,5))
ax1.hist(df[df['origin'] == 1]['mpg'], bins=10, color='Olive')
ax2.hist(df[df['origin'] == 2]['mpg'], bins=10, color='SeaGreen')
ax3.hist(df[df['origin'] == 3]['mpg'], bins=10, color='Salmon')
plt.show()



df[['mpg', 'origin', 'cylinders']].plot(by=['origin', 'cylinders'],
                                        kind='hist', figsize=(8, 30))
plt.show()

