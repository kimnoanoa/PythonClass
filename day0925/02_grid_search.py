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

# 그리드 서치
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

params = {'min_impurity_decrease' :[0.0001,0.0002,0.0003,0.0004,0.0005]}

# n_jobs -- CPU 코어 개수 최대
gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)

# 파라미터를 돌아가며 교차검증 시행
# 가장 최적의 파라미터 조합결과가 나오면, 그 조합으로 모델 최종 훈련
gs.fit(train_input,train_target)

# 가장 좋은 조합 (모델) 받아오기
dt = gs.best_estimator_ 
print('그리드 서치 종료 후 훈련셋 스코어')
print(dt.score(train_input,train_target))

print('가장 점수가 높은 조합')
print(gs.best_params_)

print('각 조합에 대한 검증점수')
print(gs.cv_results_['mean_test_score'])

print('가장 점수가 높은 조합 - 방법2')
print(gs.cv_results_['params'][gs.best_index_])

# 여러 파라미터 서치하기
params = {'min_impurity_decrease': np.arange(0.0001,0.001,0.01),
          'max_depth' : range(5,20,1),
          'min_samples_split' : range(2,100,10)}

gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
gs.fit(train_input,train_target)

# 교차검증

print('가장 점수가 높은 조합')
print(gs.best_params_)

print('가장 높은 검증 점수')
print(np.max(gs.cv_results_['mean_test_score']))

# 가장 좋은 조합 (모델) 받아오기
dt = gs.best_estimator_ 
print('그리드 서치 종료 후 훈련셋 스코어')
print(dt.score(train_input,train_target))
print('그리드 서치 종료 후 테스트셋 스코어')
print(dt.score(test_input,test_target))

# --------------랜덤 서치------------------
from scipy.stats import uniform,randint

params ={'min_impurity_decrease' : uniform(0.0001,0.001),
         'max_depth' : randint(20,50),
         'min_samples_split' : randint(2,25),
         'min_samples_leaf' : randint(1,25)}

from sklearn.model_selection import RandomizedSearchCV

rs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42),params,
                        n_iter=100, n_jobs=-1, random_state=42)
rs.fit(train_input,train_target)

print('가장 좋은 조합')
print(rs.best_params_)

print('가장 높은 검증 점수')
print(np.max(rs.cv_results_['mean_test_score']))
print()

dt = rs.best_estimator_
print('테스트셋 스코어')
print(dt.score(test_input,test_target))