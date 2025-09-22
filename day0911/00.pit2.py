# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager,rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font',family = font_name)
plt.rcParams['axes.unicode_minus'] = False

# ------------------------------------------------------------

fig, ax = plt.subplots(1,1,figsize =(8,6))
ax.plot(range(1,10),range(11,29,2),marker ='D',label='내그래프')
ax.set_title('엄청난그래프')
ax.set_xlabel('대단한가로축')
ax.set_ylabel('놀라운와이축')
ax.legend()

# plt.show()

fig,axes = plt.subplots(2,2,figsize =(10,8))
axes[0,0].plot(range(1,10),range(11,20),marker ='s')
axes[0,0].set_title('일번그래프')
axes[0,0].set_xlabel('일번엑스축')
axes[0,0].set_ylabel('일번와이축')
axes[0,0].legend(labels=['일번'])


a=[7,8,9]
sr1= pd.Series(a)
axes[0,1].plot(sr1)

sr1.plot(ax=axes[1,0],color='orange')
axes[1,0].set_xticks(range(0,11,1))
axes[1,0].set_yticks(range(0,101,10))

c = range(10,101,10)

import numpy as np
d = np.arange(100,9,-10)

df = pd.DataFrame({'숫자1':c,'숫자2':d}, index=range(10,101,10))
print(df)

axes[1,1].plot(df)
axes[1,1].annotate('엑스맨',
                   xy=(50,80),
                   size = 20)

plt.tight_layout()
plt.show()

