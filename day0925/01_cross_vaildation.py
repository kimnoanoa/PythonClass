# 결정트리 - 의사 결정 나무

import pandas as pd

wine = pd.read_csv('https://bit.ly/wine_csv_data')

print(wine.head())
wine.info()
print()
print(wine.describe())
print()

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']
print(target.unique())
print()

from sklearn.model_selection import train_test_split

# 훈련 - 테스트 나누기
train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

# 훈련셋 >> 훈련 - 검증 나누기
sub_input, val_input, sub_target, val_target = train_test_split(
    train_input, train_target, test_size=0.2, random_state=42)

print('훈련 - 검증 세트 크기')
print(sub_input.shape, val_input.shape)

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input,sub_target)

print('훈련/검증 스코어')
print(dt.score(sub_input,sub_target))
print(dt.score(val_input,val_target))

# ---------------- 교차검증 ------------------

from sklearn.model_selection import cross_validate

scores = cross_validate(dt,train_input,train_target)
print(scores)

import numpy as np
print('교차검증 평균스코어')
print(np.mean(scores['test_score']))

from sklearn.model_selection import StratifiedKFold

# 분류 디폴트 cv=StratifiedKFold() / 회귀 모델 KFold()
scores = cross_validate(dt, train_input,train_target,cv=StratifiedKFold())
print(np.mean(scores['test_score']))

# StratifiedKFold 옵션 설정
splitter = StratifiedKFold(n_splits=10, shuffle=True,random_state=42)
scores = cross_validate(t,train_input,train_target,cv=splitter)
print(np.mean(scores['test_score']))


