# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager,rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family = font_name)
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------------------------------------

a = [1,2,3]
b = [4,5,6]

s1 = pd.Series(b, name ='score')
print(s1)

df = pd.DataFrame([a,b] , index=['철수','영희'],columns=['a','b','c'])
print(df)

# plt.plot(s1)
# plt.show()

# # plt.plot (x축 자료, y축 자료)
# plt.plot([0,1,2],[6,5,3],color='blue')
# plt.plot(a,b)
# plt.show()


# plt.plot(s1,marker='o', color='red',linestyle='dotted')
# plt.show()

plt.plot([-1,1,3],[8,6,4],color ='blue',label ='파랑')
plt.plot(s1,marker='o',color='red',linestyle='dotted',label='연습직선')

plt.title('직선')
plt.xlabel('엑스라벨')
plt.ylabel('와이라벨')

plt.xlim([-2,5])
plt.ylim([2,9])
plt.xticks([0,2,3],['aaaa','bbbb','cccc'], rotation=90)

plt.annotate('이건 직선', xy = (0,5), color='red',rotation =45) # 메모/알림

# plt.legend()
# plt.show()

plt.figure(figsize=(10,8))
plt.plot([-1,1,3],[8,6,4],color='blue',label='파란직선')
plt.legend()
plt.show()

plt.plot(df.T)
plt.show()






