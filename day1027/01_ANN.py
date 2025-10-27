'''
<머신러닝>
KNN - 최근접 이웃 - 예측, 분류
리니어 리그레션, 로지스틱 리그레션 
디씨전트리 - 랜덤포레스트 - 엑스트라트리 - XGBoost 등등
SVM (서포트 벡터 머신)

뉴런
인공신경망(Artificial Neural Network) ANN
'''

# pip install keras
# pip install tensorflow

# ------------------------------------

# 패션 MNIST 데이터셋
# 10 종류의 패션 아이템
# keras - 딥러닝 고수준 API

import keras

print('\n----- 데이터셋 로드 -----')
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

# 데이터 크기 확인
print('\n----- 훈련셋 크기 -----')
print(train_input.shape, train_target.shape) # (60000, 28, 28) (60000,)
print('\n----- 테스트셋 크기 -----')
print(test_input.shape, test_target.shape) # (10000, 28, 28) (10000,)

# 이미지로 뽑아보기
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 10, figsize=(10,10))
for i in range(10):
    axs[i].imshow(train_input[i], cmap='gray_r')
    axs[i].axis('off')
plt.show()

print('\n----- 첫 10개 타겟값 -----')
print(train_target[:10]) # [9 0 0 3 0 2 7 2 5 5]

'''
0       1       2       3       4       5       6       7       8       9      
티셔츠  바지   스웨터   드레스   코트    센달    셔츠    스니커즈  가방    앵클부츠
'''

import numpy as  np

# 클래스별 데이터 개수 확인
print('\n----- 클래스별 데이터 개수 확인 -----')
print(np.unique(train_target, return_counts=True))


# ---------- 로지스틱 회귀로 패션 아이템 분류하기 ----------

# 스케일링 (이미지의 경우 보통 0~1 사이로 스케일링)
train_scaled = train_input / 255.0
# 인풋 사이즈로 리셰입
train_scaled = train_scaled.reshape(-1, 28*28)

print('\n----- 훈련셋 크기 -----')
print(train_scaled.shape) # (60000, 784)


from sklearn.model_selection import cross_validate
from sklearn.linear_model import SGDClassifier

# max_iter 10, 20 으로 변경 시도
print('\n ----- SGDClassifier 컴파일 및 교차검증 -----')
sc = SGDClassifier(loss='log_loss', max_iter=20, random_state=42)
scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)

print('\n----- 테스트 스코어 -----')
print(np.mean(scores['test_score']))


# ---------- 인공 신경망으로 모델 만들기 ----------

# 텐서플로우(구글), 파이토치(페이스북) = 저수준 백엔드 엔진
# 케라스(테서플로우를 고수준 API) 이 외에도 텐서플로우를 쓸 수있는 여러가지 API가 있었으나
# 이제 거의 텐서플로우 = 케라스 와 같은 의미가 됨.

from sklearn.model_selection import train_test_split

# 위에서 만든 훈련셋에서 또다시 검증세트 떼어내기.
train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# 데이터 크기 확인
print('\n----- 훈련세트 크기 -----')
print(train_scaled.shape, train_target.shape)
print('\n----- 검증세트 크기 -----')
print(val_scaled.shape, val_target.shape)

inputs = keras.layers.Input(shape=(784,)) # 입력층
dense = keras.layers.Dense(10, activation='softmax')
# 밀집층 (중에서 출력층), 완전 연결층
# softmax - 활성화 함수
# 파라미터 = 784x10 + 10 = 7850
model = keras.Sequential([inputs, dense])

# ---------- 인공신경망으로 패션 아이템 분류하기 ----------

'''
categorical_crossentropy -> 원-핫 인코딩된 라벨 필요
sparse_categorical_crossentropy -> 정수 인코딩된 라벨만 주면 됨.
  - 내부적으로 원핫인코딩을 자동으로 처리한 것과 동일하게 로스 계산

이진 분류는 binary_crossentropy
'''

# 모델 컴파일
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(train_target[:10]) # [7 3 5 8 6 9 3 3 9 9] 정수 라벨링이지만 괜찮다.

print('\n----- 모델 훈련 -----')
model.fit(train_scaled, train_target, epochs=5)

'''
학습데이터 48000 개
model.fit(x, y, epochs=5) -> batch_size=32 기본 적용
배치사이즈? - 배치사이즈만큼 데이터를 주입후 파라미터 1번 업데이트
한번의 에포크에서 48000 / 32 = 1500 번의 파라미터 업데이트가 일어남.
필요하다면 model.fit(...., batch_size=64) 
'''

# 모델 평가 evaluate
print('\n----- 모델 평가 -----')
print(model.evaluate(val_scaled, val_target))

