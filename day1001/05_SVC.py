# SVM (support vector machine) - 분류계의 전통강자
# 분류 SVC, (회귀) 예측 SVR
# 결정경계를 찾는 모델
# 마진 - 서포트 벡터와 결정 경계와의 거리
# 마진을 최대화 하는 것을 목표로 함

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X, y = make_classification(n_samples=400, n_classes=2, n_features=2,
                           n_redundant=0, random_state=42)

# n_samples   총샘플 수
# n_classes   클래스 수
# n_features  특성 수
# n_redundant 불필요한 특성 수

print(X)
print()
print(y)
print()

# 훈련셋 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# 스케일링
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

# 선형 커널 
lin_clf = SVC(kernel='linear', C=1.0, random_state=42)  # 모델 세팅  # C 값 높을 수록 예민하다 (과대적합)
lin_clf.fit(X_train_sc, y_train)                        # 모델 훈련
y_pred_lin = lin_clf.predict(X_test_sc)                 # 예측

print('LinearSVC 정확도: ', accuracy_score(y_test, y_pred_lin))
print(classification_report(y_test, y_pred_lin))
print('혼동행렬: \n', confusion_matrix(y_test, y_pred_lin))
print()

# RBF 커널 (비선형 경계학습)
# Redial Basis Function (방사 기저 함수)

# gamma 값이 높을 수록 (과적합 위험)
rbf_clf = SVC(kernel='rbf', C=1.0, gamma=0.1, random_state=42)
rbf_clf.fit(X_train_sc, y_train)
y_pred_rbf = rbf_clf.predict(X_test_sc) 

print('RBF SVC 정확도: ', accuracy_score(y_test, y_pred_rbf))
print(classification_report(y_test, y_pred_rbf))
print('혼동행렬: \n', confusion_matrix(y_test, y_pred_rbf))
print()


