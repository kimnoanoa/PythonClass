'''
CNN - Convolutional Neural Network
합성곱(Convolution) - 입력 이미지에 필터를 적용하여 특징(경계, 패턴 등)을 추출하는 연산.
특성맵(Feature Map) - 필터가 입력을 통과한 결과로, 해당 필터가 감지한 특징의 강도를 나타내는 출력.

패딩(Padding) - 합성곱 연산 신 이미지 가장자리 정보 손실을 막기 위해 입력 주변에 0 등을 채우는 기법.
스트라이드(Stride) - 필터가 한 번에 이동하는 칸 수로, 값이 클수록 출력 크기가 작아짐.
'''

# ================================================================

import keras
import tensorflow as tf

keras.utils.set_random_seed(42)
tf.random.set_seed(42)
tf.config.experimental.enable_op_determinism()

from sklearn.model_selection import train_test_split

print('\n----- 패션 MNIST 데이터 로드 -----')
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

print('\n----- train_input 크기 -----')
print(train_input.shape) # (60000, 28, 28)

# 케라스 합성곱 층에 넣으려면,,, 기본적으로 3차원(구조) 입력을 기대 
# 컬러 이미지는 채널이 3개(RGB) 이기 때문
# 컴퓨터 비전 분야에서의 규칙 - 데이터 배열 (이미지수, 세로, 가로, 채널)
train_scaled = train_input.reshape(-1, 28, 28, 1) / 255.0
print('\n----- 3차원 변환 후 크기 -----')
print(train_scaled.shape)

train_scaled, val_scaled, train_target, val_target, = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)

# ---------- 합성곱 신경망 만들기 ----------

model = keras.Sequential()
model.add(keras.layers.Input(shape=(28,28,1))) # 3차원 입력 기대
model.add(keras.layers.Conv2D(32, kernel_size=3, # 도장 32개, 커널사이즈 3x3
                              activation='relu', padding='same'))
# >>> 28 x 28 x 32 (특성맵 32장)
model.add(keras.layers.MaxPooling2D(2)) # 4개 중 가장 큰값으로 대체
# >>> 14 x 14 x 32

model.add(keras.layers.Flatten()) # 일렬로 펼친다
# 6272 (14 x 14 x 32) 
model.add(keras.layers.Dense(100, activation='relu')) # 은닉층 (뉴런 100개)
model.add(keras.layers.Dropout(0.4)) # 드랍아웃
model.add(keras.layers.Dense(10, activation='softmax')) # 출력층 (클래스 10개)

print()
model.summary()

# 3x3x32 + 32 = 320
# 6272 x 100 + 100 = 627300
# 100 x 10 + 10 = 1010

# 결국에는 어떤 구조와 숫자(파라미터)를 세팅해서 적정한 숫자를 찾아가는 것.
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.keras',
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)

print('\n----- 모델훈련 -----')
history = model.fit(train_scaled, train_target, epochs=20,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb])

import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()

print('\n----- 모델 evaluate -----')
print(model.evaluate(val_scaled, val_target)) # accuracy: 0.9142 - loss: 0.2457

# (검증) 첫번째 사진 그림으로 확인
print('\n 첫번째 사진 차원:', val_scaled[0].shape) # 28 x 28 x 1

plt.imshow(val_scaled[0].reshape(28, 28), cmap='gray_r')
plt.show()  # 실제 사진 = 가방

print('\n----- 첫번째 사진 예측 -----')
preds = model.predict(val_scaled[0:1]) # 슬라이싱으로 넣어줘야 (1, 28, 28, 1)로 전달된다.
print(preds)
'''
[[7.2914687e-17 3.3638042e-25 2.8963967e-18 1.6334074e-17 6.5324464e-15
  6.6230176e-18 3.0252314e-14 8.2424554e-16 1.0000000e+00 6.5238850e-21]]
'''

# 위 확률을 그래프로 확인
plt.bar(range(1,11), preds[0])
plt.xlabel('class')
plt.ylabel('prob')
plt.show()

classes = ['티셔츠', '바지', '스웨터', '드레스', '코트',
           '샌달', '셔츠', '스니커즈', '가방', '앵클부츠']

import numpy as np

print('\n----- 예측 클래스 -----')
print(classes[np.argmax(preds)])

# 테스트셋으로 테스트 실시

test_scaled = test_input.reshape(-1, 28, 28, 1) / 255.0

print('\n----- 테스트 데이터셋 크기 -----')
print(test_scaled.shape)

print('\n----- 테스트 점수 -----')
print(model.evaluate(test_scaled, test_target))