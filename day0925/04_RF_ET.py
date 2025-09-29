import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

# 데이터 불러오기

data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

print(X.head())
X.info()
print(y.head())

# 훈련/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 정의 (두개죠)
rf_model = RandomForestRegressor(random_state=42)
et_model = ExtraTreesRegressor(random_state=42)

# 하이퍼파라미터 그리드 설정
param_grid = {
    'n_estimators': [50, 100],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5]
}

# 그리드 서치 설정 (verbose=3 까지 설정 가능)
rf_grid = GridSearchCV(rf_model, param_grid, n_jobs=-1, verbose=1)
et_grid = GridSearchCV(et_model, param_grid, n_jobs=-1, verbose=1)

# 모델 학습
print('랜덤포레스트 그리드 서치')
rf_grid.fit(X_train, y_train)
print()

print('엑스트라트리 그리드 서치')
et_grid.fit(X_train, y_train)
print()

# 최적의 파라미터 출력
print('랜덤포레스트 best: ', rf_grid.best_params_)
print('엑스트라트리 best: ', et_grid.best_params_)

# 최적 모델
rf_best = rf_grid.best_estimator_
et_best = et_grid.best_estimator_

# 성능평가
print('랜덤포레스트 스코어: ', rf_best.score(X_test, y_test))
print('엑스트라트리 스코어: ', et_best.score(X_test, y_test))


