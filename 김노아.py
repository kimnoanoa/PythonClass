# 머신러닝 분류모델 학습 코드를 작성하시오.

# =======================================

# 타이타닉 데이터를 이용하여,
# 수업시간에 배운 머신러닝 모델 2가지를 학습 시킨뒤,
# 성능을 비교/평가하세요.

# <코드>
# 전처리 및 간단한 시각화
# 최적의 파라미터를 찾기 위한 그리드 서치 시행
# 다양한 성능평가시 ROC 그래프 필수 포함


# 코드를 완성하고 결과를 ppt에 정리하세요. (사진 + 설명)

# <ppt>
# 데이터 전처리를 왜 그렇게 하엿는지 이유를 상세히 기술하세요.
# 각종 시각화, 그래프, 터미널 출력화면 등 이미지 삽입 (+ 설명)
# 발표용이 아닌 채점용이므로 디자인은 하지 않아도 됩니다.

# !! 수업시간에 배운 내용들로 하세요 !!

# =======================================

# <제출>
# 홍길동.py
# 홍길동.pptx

# 위 두 파일을 압축하지 말고 디스코드 메세지로 보내 주세요.
# (TMS 업로드는 10/13 에 진행 예정)

# =======================================

# 평가 - 오전
# 수업 - 오후1
# 면담 & 프로젝트 팀 발표 - 오후2

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, roc_curve, auc, RocCurveDisplay
)

df = sns.load_dataset('titanic')

# 데이터 불러오기
df = sns.load_dataset('titanic')

# 필요한 열만 사용
df = df[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']]

# 결측치 처리
# 나이에 결측치가 있을 경우 그 중간값으로 처리함
# 탑승항구 데이터에 결측치가 있을 경우 최빈값으로 처리함
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])

# 범주형 인코딩 (문자열 데이터 수치형 변수로 변환 처리)
df = pd.get_dummies(df, drop_first=True)

# 타이타닉의 사망자와 생존자를 예측하는 모델

# 학습/테스트 분리 (학습용 80, 테스트용 20)
X = df.drop('survived', axis=1)
y = df['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)


# -------------의사결정나무 모델 객체 생성-------------

# random_state=42를 설정하면 동일한 결과를 재현할 수 있음 (랜덤성 통제)
dt_model = DecisionTreeClassifier(random_state=42)

# 하이퍼파라미터 후보들을 정의
# - max_depth: 트리의 최대 깊이 (깊어질수록 복잡한 모델, 과적합 위험 증가)
# - min_samples_split: 노드를 분할할 최소 샘플 수 (작을수록 트리 분할이 활발히 일어남)
param_grid = {
    'max_depth': [3, 5, 10, None],          # None이면 최대한 깊게 분할
    'min_samples_split': [2, 5, 10]         # 최소 샘플 수 설정
}
# GridSearchCV: 모든 조합의 하이퍼파라미터를 테스트하여 최적 조합을 찾음
# - cv: 교차검증 방식으로 StratifiedKFold 사용 (클래스 비율 유지됨)
# - scoring: 성능 기준은 정확도(accuracy)
grid_dt = GridSearchCV(
    estimator=dt_model,          # 모델
    param_grid=param_grid,       # 하이퍼파라미터 후보들
    cv=StratifiedKFold(n_splits=5),  # 교차검증: 데이터를 5개로 나누고 5번 반복
    scoring='accuracy'           # 평가 기준: 정확도
)

# 학습 데이터(X_train, y_train)로 그리드서치 수행
# 내부적으로 5-fold 교차검증을 통해 모든 조합을 평가함
grid_dt.fit(X_train, y_train)

# 최적의 하이퍼파라미터를 사용한 모델 추출
# (교차검증 결과 가장 성능이 좋았던 조합)
best_dt = grid_dt.best_estimator_

# 테스트 데이터(X_test)에 대해 예측 수행
# → 결과는 생존 여부를 나타내는 클래스 값 (0 또는 1)
y_pred_dt = best_dt.predict(X_test)

# ROC 곡선을 그리기 위해 클래스 확률값(1일 확률)을 추출
# → predict_proba는 [0일 확률, 1일 확률] 반환하므로, [1]만 사용
y_proba_dt = best_dt.predict_proba(X_test)[:, 1]

from sklearn.tree import plot_tree

# 의사결정나무 시각화
plt.figure(figsize=(20,10))
plot_tree(best_dt, 
          feature_names=X.columns,  
          class_names=['Died', 'Survived'],  
          filled=True,  
          rounded=True,
          fontsize=10)
plt.title('Decision Tree Visualization')
plt.show()



# -------------랜덤 포레스트 분류기 객체 생성----------------

# 여러 개의 결정 트리를 앙상블하여 과적합을 줄이고 일반화 성능을 높임
# random_state는 결과 재현을 위해 고정
rf_model = RandomForestClassifier(random_state=42)

# 하이퍼파라미터 그리드 정의
# n_estimators: 생성할 트리의 개수
# max_depth: 트리의 최대 깊이
# min_samples_split: 노드를 분할할 최소 샘플 수
param_grid_rf = {
    'n_estimators': [100, 200],       # 트리 수
    'max_depth': [3, 5, 10],          # 트리 깊이 제한
    'min_samples_split': [2, 5]       # 분할 최소 샘플 수
}

# 최적의 하이퍼파라미터 조합을 찾기 위한 GridSearchCV 설정
# StratifiedKFold: 각 fold에서 클래스 비율을 유지하며 교차검증
# scoring='accuracy': 평가 기준은 정확도
grid_rf = GridSearchCV(
    rf_model,                        # 사용할 모델
    param_grid_rf,                   # 하이퍼파라미터 후보
    cv=StratifiedKFold(n_splits=5), # 5겹 교차검증 (계층화)
    scoring='accuracy'              # 정확도를 기준으로 최적 모델 탐색
)

# 학습 데이터를 이용해 그리드서치 실행
# 내부적으로 각 하이퍼파라미터 조합에 대해 5번씩 학습 후 평균 성능 평가
grid_rf.fit(X_train, y_train)

# 가장 성능이 좋았던 모델 추출
best_rf = grid_rf.best_estimator_

# 테스트 세트에 대해 예측 수행 (클래스 예측: 0 또는 1)
y_pred_rf = best_rf.predict(X_test)

# 테스트 세트에 대해 확률 예측 수행 (ROC Curve 등을 위해 사용)
# [:, 1] → 생존(클래스 1)일 확률만 추출
y_proba_rf = best_rf.predict_proba(X_test)[:, 1]

# 랜덤포레스트 시각화
import numpy as np

importances = best_rf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10,6))
plt.title('Feature Importances in Random Forest')
plt.bar(range(len(importances)), importances[indices], color='skyblue', align='center')
plt.xticks(range(len(importances)), X.columns[indices], rotation=45, ha='right')
plt.tight_layout()
plt.show()


# roc_curve, auc 함수 import
from sklearn.metrics import roc_curve, auc  

# 모델 성능 평가 함수 정의
def evaluate_model(y_test, y_pred, y_proba, model_name):
    print(f"----- {model_name} -----")
    print("Accuracy:", accuracy_score(y_test, y_pred)) # 정확도
    print("Precision:", precision_score(y_test, y_pred)) # 정밀도
    print("Recall:", recall_score(y_test, y_pred)) # 재현율
    print("F1 Score:", f1_score(y_test, y_pred)) # F1스코어 출력
    print(classification_report(y_test, y_pred)) # 상세 분류 보고서 출력
    
    # ROC Curve 계산을 위한 FPR, TPR, Threshold 구하기
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    
    # AUC (Area Under Curve) 계산
    auc_score = auc(fpr, tpr)
    
    # ROC Curve 그래프에 모델 이름과 AUC 점수를 라벨로 붙여서 플롯
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {auc_score:.2f})')

plt.figure(figsize=(8,6))

# Decision Tree 모델 평가 및 ROC Curve 그리기
evaluate_model(y_test, y_pred_dt, y_proba_dt, "Decision Tree")

# Random Forest 모델 평가 및 ROC Curve 그리기
evaluate_model(y_test, y_pred_rf, y_proba_rf, "Random Forest")

# 대각선 점선 (무작위 분류 기준)
plt.plot([0,1], [0,1], 'k--')

plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')

# 범례 표시 (모델 이름과 AUC 값)
plt.legend()
# 그리드 표시
plt.grid()
plt.show()

