from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

# 데이터셋 준비
dataset = load_diabetes()

X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
y = pd.Series(dataset.target, name='target')

print(X.head())
print(y.head())

# 데이터셋 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 모델 (확률적 경사하강)
reg = SGDRegressor(
    loss='squared_error',
    penalty='l2', # 규제 방법
    alpha=0.0001, # 규제 강도
    max_iter=2000, # 최대 반복 횟수 (2000번 안넘음)
    tol=1e-3, # 허용오차 (손실이 이숫자보다 작으면 학습 멈춤)
    random_state=42 # 시드번호 42 (랜덤 재현)
)

# 학습
reg.fit(X_train_scaled, y_train)

# 예측
y_pred = reg.predict(X_test_scaled)

# 성능지표
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("[Regression Metrics]")
print(f'MAE : {mae:.4f}') # 평균 절대 오차
print(f'MSE : {mse:.4f}') # 평균 제곱 오차
print(f'RMSE : {rmse:.4f}') # 루트 평균 제곱 오차
print(f'R^2 : {r2:.4f}')  # 결정계수 (1에 가까울수록 좋음)
print(f'score : {reg.score(X_test_scaled, y_test):.4f}') # 결정계수




