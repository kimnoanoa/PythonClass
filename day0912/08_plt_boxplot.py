import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager,rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family = font_name)
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./data/auto-mpg.csv', header=None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
plt.style.use('grayscale')

# ------------------------------------------------------------

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(15,5))

ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA','EU','JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],
               labels=['USA','EU','JAPAN'],
               vert=False)

ax1.set_title('제조국가별 연비 분포(수직 박스플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스플롯)')

# df.plot(kind='box',column=['mpg','weight'],by=['origin'],figsize=(15,5))

fig, axes = plt.subplots(1,2,figsize=(15,5))
df.plot(kind='box',column=['mpg'],by=['origin'],ax = axes[0])
axes[0].set_title('제조국가별 연비 분포(수직 박스플롯)')
axes[0].set_xticklabels(['USA','EU','JAPAN'])

df.plot(kind='box',column=['mpg'],by=['origin'],ax = axes[1] , vert=False)
axes[1].set_title('제조국가별 연비 분포(수평 박스플롯)')
axes[1].set_yticklabels(['USA','EU','JAPAN'])

plt.show()

# 박스플롯 - 색상지정

color = {
    'boxes':'SeaGreen',
    'whiskers':'Olive',
    'medians':'Teal',
    'caps':'Blue'
}

df.plot(kind='box', column=['mpg'],by=['origin'],figsize=(15,5),
        color = color, sym='r+', vert=False)
plt.show()

