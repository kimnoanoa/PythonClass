# 앙상블(두명 이상이 함께 연주하는)
# random forest (랜덤포레스트)
# 100개의 결정트리 - 분류(다수결) /예측(평균)
# 부트스트랩 샘플(중복허용 랜덤추출)
# 특성선택 - 랜덤선택

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wine = pd.read_csv('https://bit.ly/wine_csv_data')
data = wine[['alcohol','sugar','pH']]
target = wine['class']

train_input , test_input , train_target , test_target = train_test_split(
    data, target, test_size=0.2, random_state=42
)
print('인풋데이터 개수')
print(train_input.shape)

from sklearn.model_selection import cross_validate
from sklearn.ensemble import RandomForestClassifier

# 100그루의 나무
# 5197 개의 데이터에서 각각 나무들은 5197개의 랜덤(중복) 데이터를 뽑음.

rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf,train_input,train_target,return_train_score=True,n_jobs=-1)

# 5번의 교차검증에 대한 훈련/검증 스코어 평균
print(np.mean(scores['train_score']), np.mean(score['test_score']))

rf.fit(train_input,train_target)
print('랜덤포레스트 특성 중요도')
print(rf.feature_importances_)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_input,train_target)

print('결정나무 특성 중요도')
print(dt.feature_importances_)

# ---------------- 엑스트라 트리 ------------------



