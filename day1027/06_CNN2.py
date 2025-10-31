# 이전 절에서 저장한 모델 불러오기
import keras
model = keras.models.load_model('best-cnn-model.keras')
print('\n----- 모델 레이어 출력 -----')
print(model.layers)

# 첫번째 합성곱층 가중치/편향 출력
conv = model.layers[0]
print('\n----- 첫번째 합성곱층 가중치/편향 크기 -----')
print(conv.weights[0].shape, conv.weights[1].shape)

# 첫번째 합성곱층 가중치의 평균과 표준편차 출력
conv_weights = conv.weights[0].numpy()
print('\n----- 첫번째 합성곱층 가중치의 평균/표준편차 -----')
# 0을 중심으로 잘 학습 되었다. 
print(conv_weights.mean(), conv_weights.std())

# 그래프로 출력
import matplotlib.pyplot as plt

plt.hist(conv_weights.reshape(-1, 1)) # 4차원을 1차원으로
plt.xlabel('weight')
plt.ylabel('count')
plt.show()

# 32개의 커널을 직접 출력해보기
fig, axs = plt.subplots(2, 16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i, j].imshow(conv_weights[:,:,0,i*16 + j], vmin=-0.5, vmax=0.5)
        axs[i, j].axis('off')
plt.show()
# [:,:,0,0] 에서 [:,:,0,31] 까지 출력

# ================================================================

# 빈 합성곱 신경망 만들어서 똑같이 진행

no_training_model = keras.Sequential()
no_training_model.add(keras.layers.Input(shape=(28,28,1)))
no_training_model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu',
                                          padding='same'))

no_training_conv = no_training_model.layers[0]
print('\n----- 빈 합성곱 첫번째 층 가중치 크기 -----')
print(no_training_conv.weights[0].shape) # (3, 3, 1, 32)

no_training_weights = no_training_conv.weights[0].numpy()
print('\n----- 빈 합성곱 가중치 평균/표준편차 -----')
print(no_training_weights.mean(), no_training_weights.std()) # 표준 편차가 너무 작음

plt.hist(no_training_weights.reshape(-1, 1))
plt.xlabel('weight')
plt.ylabel('count')
plt.show()

fig, axs = plt.subplots(2, 16, figsize=(15,2))
for i in range(2):
    for j in range(16):
        axs[i, j].imshow(no_training_weights[:,:,0,i*16 + j], vmin=-0.5, vmax=0.5)
        axs[i, j].axis('off')
plt.show()

# =================================================================

# 함수형 API를 이용하여 중간에 특성맵 뽑아서 그려보기

# 함수형 API 예시
inputs = keras.Input(shape=(784,))
dense1 = keras.layers.Dense(100, activation='relu')
dense2 = keras.layers.Dense(10, activation='softmax')

hidden = dense1(inputs)
outputs = dense2(hidden)

func_model = keras.Model(inputs, outputs)

# ---------------------------------------------------------

# 모델의 인풋층 
print('\n',model.inputs)

# 첫 합성곱층까지 함수형 API로 잘라서 만들기.
conv_acti = keras.Model(model.inputs, model.layers[0].output)

# 특성맵 시각화
(train_input, train_target), (test_input, test_target) =\
    keras.datasets.fashion_mnist.load_data()

# 첫번째 이미지 확인 (앵클부츠)
plt.imshow(train_input[0], cmap='gray_r')
plt.show()

ankle_boot = train_input[0:1].reshape(-1, 28, 28, 1) / 255.0
feature_maps = conv_acti.predict(ankle_boot) # 잘라 만든 모델에 이미지 넣기 >> 특성맵 32장

print('\n----- 첫 합성곱층 통과후 크기 -----')
print(feature_maps.shape) # (1, 28, 28, 32)

fig, axs = plt.subplots(4, 8, figsize=(15, 8))
for i in range(4):
    for j in range(8):
        axs[i, j].imshow(feature_maps[0,:,:,i*8 + j])
        axs[i, j].axis('off')
plt.show()

# 두번째 합성곱 층이 만든 특성맵 확인하기
conv2_acti = keras.Model(model.inputs, model.layers[2].output)
feature_maps = conv2_acti.predict(ankle_boot)

print('\n----- 두번째 합성곱 통과후 모양 -----')
print(feature_maps.shape) # (1, 14, 14, 64)

fig, axs = plt.subplots(8, 8, figsize=(12,12))
for i in range(8):
    for j in range(8):
        axs[i, j].imshow(feature_maps[0,:,:,i*8 + j])
        axs[i, j].axis('off')
plt.show()