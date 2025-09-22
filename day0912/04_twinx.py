import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

from matplotlib import font_manager, rc
#한글표기
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
# 음수표기
plt.rcParams['axes.unicode_minus'] = False
# 터미널 너비
pd.set_option('display.width', 500)

# --------------------------------------------------------------------

plt.style.use('ggplot')

df = pd.read_excel('./data/남북한발전전력량.xlsx')
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis=1, inplace=True)
df.set_index('발전 전력별', inplace=True)

print(df)
print()
df = df.T
print(df)
print()

df['원자력'] = df['원자력'].replace('-', '0')
df = df.replace('-', '0')
print(df)
df.info()
print()

df = df.astype(float)

df = df.rename(columns={'합계':'총발전량'})
df['총발전량 - 1년'] = df['총발전량'].shift(1)
print(df)
print()
df['증감율'] = ((df['총발전량']-df['총발전량 - 1년'])/df['총발전량 - 1년']) * 100
print(df)
print()
df.info()


ax1 = df[['수력', '화력']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True)
ax2 = ax1.twinx() # x축을 공유
ax2.plot(df.index, df['증감율'], ls='--', marker='o', markersize=20, 
         color='green', label='전년대비 증감율(%)')  


# plt.plot(df.index, df['증감율'], ls='--', marker='o', markersize=20, 
#          color='green', label='전년대비 증감율(%)')  


plt.show()


