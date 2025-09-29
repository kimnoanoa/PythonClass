'''
Accuracy(정확도): 전체 중 맞춘 비율. 클래스 불균형에 취약.
Precision(정밀도): 모델이 양성이라 한 것 중 실제 양성 비율. 가짜양성(FP)를 줄여라!
Recall(재현율/민감도): 실제 양성을 잡아낸 비율. 놓침(FN)을 줄여라!
F1-score: 정밀도, 재현율의 조화평균. 둘의 균형을 평가
FPR(위양성률) - 스팸이 아닌데 스팸으로 분류된 비율
ROC, AUC: 임계값 전 구간에 대한 분류력(민감도 vs 1-특이도).
'''

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score,\
f1_score, roc_auc_score, confusion_matrix, classification_report, RocCurveDisplay
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target, name='target')

# 악성이 0 으로 되어있어서, 0과 1 자리 바꾸기
y = 1 - y

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=1)

# 모델 훈련
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)

# 예측 및 확률
y_pred = dt.predict(X_test)
print('y_pred:\n', y_pred)
y_proba = dt.predict_proba(X_test)[:,1]
print('y_proba:\n', y_proba)

# 지표 계산
acc = accuracy_score(y_test, y_pred)
pre = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)

print("[Metrics]")
print(f'Accuracy : {acc:.4f}')
print(f'Precision: {pre:.4f}')
print(f'Recall   : {rec:.4f}')
print(f'F1-score : {f1:.4f}')
print(f'ROC AUC  : {auc:.4f}')
print()

print('Confusion Matrix')
print(confusion_matrix(y_test, y_pred))
print()

print('Classification Report')
print(classification_report(y_test, y_pred, digits=4))



''' 양성 - 암환자
TP (진짜 양성): 암환자를 잘 찾아냄
FN (가짜 음성): 암환잔데 아니라고 분류 (놓침)
FP (가짜 양성): 암환자 아닌데 맞다고 분류 (오해)
TN (진짜 음성): 아닌사람 아닌걸로 분류
'''

'''
Confusion Matrix
[71  1]   TP   FN
[ 5 37]   FP   TN
============================================
재현율 (Recall)
Recall = TP / (TP + FN)

실제 악성 중에서 모델이 놓치지 않고 잡아낸 비율
값이 높을 수록 암환자를 놓치지 않는다는 의미
FN(놓친 악성)이 줄어들 수록 Recall↑
=============================================
위양성률 (False Positive Rate, FPR)
FPR = FP / (FP + TN)

"스팸메일 아닌데 스팸으로 분류한 비율"
값이 높을 수록 (일반메일을) 스팸으로 판단하는 경우가 많다는 뜻
ROC 곡선의 X축이 FPR 이다.
=============================================
모델의 임계값(threshhold)을 조정하면 Recall과 FPR이 trade-off 관계를 가진다
임계값을 낮추면: Recall↑ (많이 잡음) but FPR↑ (오진도 늘어남)
임계값을 올리면: Recall↓ (놓침 많음) but FPR↓ (오진 줄어듦)
=============================================
정밀도 (Precision)
Precision = TP / (TP + FP)

모델이 악성이라고 예측한 것 중에서 실제 악성 비율
FP를 줄이자 -> 판정의 신뢰도
=============================================

Classification Report
              precision    recall  f1-score   support

           0     0.9342    0.9861    0.9595        72
           1     0.9737    0.8810    0.9250        42

    accuracy                         0.9474       114
   macro avg     0.9539    0.9335    0.9422       114
weighted avg     0.9488    0.9474    0.9468       114
==============================================

f1-score - precision과 recall의 조화 평균 (특징: 둘다 높아야 높게나온다.)
하나라도 낮으면 점수 낮게나옴. 물론 둘다 낮아도 낮게 나옴.

support - 해당 클래스의 실제 샘플 개수 (데이터 분포 확인용)

accuracy
전체 샘플 중에서 맞춘 비율 (정확도)

macro avg
클래스별 지표(precisin, recall, f1)를 단순 평균.
클래스 비율이 불균형일 때 '클래스마다 동일한 중요도'를 줌.

weighted avg
클래스별 지표를 support(샘플수)로 가중 평균
데이터 분포를 반영해서 평균 내므로 accuracy와 비슷한 경향.
'''

# ROC 곡선
# 모든 가능한 임계점들을 넣어보면서 정밀도, 위양성률을 계산하여 그래프 그림.
# AUC = ROC 곡선 아래 면적
RocCurveDisplay.from_predictions(y_test, y_proba)
plt.title('ROC Curve (RandomForest)')
plt.show()