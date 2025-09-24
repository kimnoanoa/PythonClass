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

# ------------------------------------------------------------
# 로지스틱 회귀로 다중분류 수행
# C = 계수제곱규제(L2), 작을 수록 규제 커짐. 기본값 1 
# max_iter 기본값 100

import numpy as np
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)

print('훈련 스코어')
print(lr.score(train_scaled, train_target))
print('테스트 스코어')
print(lr.score(test_scaled, test_target))
print()

print('상위 5개행 예측 결과')
print(lr.predict(test_scaled[:5]))
print()

print('상위 5개행 클래스별 확률')
proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))
print()

print('클래스 종류')
print(lr.classes_)

# 파라미터가 7세트 나온다.
# 각 클래스별로 방정식 만들어졌다는 뜻.
print('파라미터 개수')
print(lr.coef_.shape, lr.intercept_.shape)

'''
로지스틱회귀 모델은 - 이진분류, 다중분류가 가능하다
선형 방정식 -> 시그모이드 통과 (확률값으로 표시)
최적화 - 경사하강법 기반

이진분류
-손실함수 = 바이너리 크로스 엔트로피 (BCE)

다중분류 - 확률값 -> 소프트맥수함수 통과 (클래스별 확률값으로 표시)
- 손실함수 = 크로스 엔트로피 (CE)
'''

print('상위 5개행 클래스별 z값 출력')
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))
print()

from scipy.special import softmax

print('소프트 맥스 함수에 z값 대입')
proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))



