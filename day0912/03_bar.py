import matplotlib.pyplot as plt
import pandas as pd

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

df = pd.read_excel('data/시도별_전출입_인구수.xlsx')

print(df.head())
print()

df = df.ffill()
print(df.head()) 
print()

# 전출지 = 서울, 전입지 = 서울빼고  -->> 서울을 나간사람들 (네튤농 - 순정)

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul = df_seoul.rename({'전입지별':'전입지'}, axis=1)
df_seoul = df_seoul.set_index('전입지')
print(df_seoul)
print()

col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
print(df_4)
df_4 = df_4.T

# 스타일 지정
plt.style.use('Solarize_Light2')

# 막대 그래프 그리기
df_4.plot(kind='bar', figsize=(16,8), width=0.5, 
          color=['orange', 'green', 'skyblue', 'blue'])

plt.title('서울 -> 타시도 인구 이동', pad=10, size=30, fontweight='bold', color='brown')
plt.ylabel('이동 인구수', labelpad=10, size=20)
plt.xlabel('기간', labelpad=10, size=20)
plt.ylim(5000, 30000)
plt.tick_params(axis='x', rotation=0)
plt.legend(title='전입지', fontsize=15)
plt.show()

# ------------------- 가로형 막대 그래프 -----------------

col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
print(df_4)
print()

df_4['합계'] = df_4.sum(axis=1)
print(df_4)
print()

df_total = df_4[['합계']].sort_values(by='합계', ascending=True)
print(df_total)

df_total.plot(kind='barh', figsize=(10, 5))
plt.title('서울 -> 타시도 인구이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')
plt.show()

fig, axes = plt.subplots(1,2,figsize=(10,5))
axes[0].bar(df_total.index, df_total['합계'])
df_total.plot(kind='bar',ax=axes[1])
plt.show()