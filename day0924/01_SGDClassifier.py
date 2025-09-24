# Stochastic Gradient Descent(SGD) - 확률적 경사하강법

import pandas as pd

fish = pd.read_csv('https://bit.ly/fish_csv_data')
print(fish.head())
print()

# 물고기 종류 확인 (7개)
print(pd.unique(fish['Species']))
print()

'''
'Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt'
참붕어 붉은줄납줄개  백어      파르키    농어   가시고기   빙어
'''

# 인풋 데이터
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']]

print(fish_input.head())
print()

# 타겟 데이터
fish_target = fish['Species']

# 훈련/테스트 셋 분리 (디폴트 몇대몇? 75:25)
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)

# 스케일링(표준화)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# ----------------------------------------------------------

# 확률적 경사하강법
from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log_loss', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)

# max_iter = 10  >>> 10 에포크 (전체 데이터 10번) --- 다 채웠다면 업데이트는 총몇번? 데이터개수 X 10번
print('훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('테스트셋 스코어')
print(sc.score(test_scaled, test_target))

# 추가 학습
# 모든 데이터 1개씩 돌아가며 1회 학습 (1 에포크)
sc.partial_fit(train_scaled, train_target)
sc.partial_fit(train_scaled, train_target)

print('추가학습 훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('추가학습 테스트셋 스코어')
print(sc.score(test_scaled, test_target))


import numpy as np

sc = SGDClassifier(loss='log_loss', random_state=42)

train_score = []
test_score = []

classes = np.unique(train_target)

import matplotlib.pyplot as plt

for _ in range(0, 300):

    sc.partial_fit(train_scaled, train_target, classes=classes) # 1 에포크 학습
    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))

plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()

'''
1 에포크 -- 전체 데이터 1회 순회
옵션 max_iter=10 -- 10 에포크
1 이터레이션 -- 1회 '학습'
'''

# 100번이 적당해 보인다.
sc = SGDClassifier(loss='log_loss', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)

print('100번 훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('100번 테스트셋 스코어')
print(sc.score(test_scaled, test_target))

# tol 값 지정해보기 (손실 개선량)
sc = SGDClassifier(loss='log_loss', max_iter=200, tol=1e-4, 
                   random_state=42, n_iter_no_change=20)
sc.fit(train_scaled, train_target)

print('n번 훈련셋 스코어')
print(sc.score(train_scaled, train_target))
print('n번 테스트셋 스코어')
print(sc.score(test_scaled, test_target))
print('훈련 에포크수')
print(sc.n_iter_)