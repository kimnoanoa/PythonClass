import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# 비행기, 자동차, 새, 고양이, 사슴, 개, 개구리, 말, 배, 트럭
# CIFAR-10 데이터셋 불러오기
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # 0~1 정규화
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

print('\n----- 훈련셋 크기 -----')
print(x_train.shape) # (50000, 32, 32, 3)

print('\n----- 테스트셋 크기 -----')
print(y_train.shape) # (50000, 10)

print('\n----- 훈련셋 출력 -----')
print(x_train[0])

fig, axs = plt.subplots(1, 10, figsize=(10,10))
for i in range(10):
    axs[i].imshow(x_train[i])
    axs[i].axis('off')
plt.show()

# CNN 모델 구성
model = keras.Sequential()
model.add(keras.layers.Input(shape=(32,32,3)))  # 컬러 이미지 32x32x3

# 1번째 Conv + MaxPool
model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

# 2번째 Conv + MaxPool
model.add(keras.layers.Conv2D(64, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

# 3번째 Conv + MaxPool
model.add(keras.layers.Conv2D(128, kernel_size=3, activation='relu', padding='same'))
model.add(keras.layers.MaxPooling2D(2))

# Flatten & Dense
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dropout(0.4))
model.add(keras.layers.Dense(10, activation='softmax'))

model.summary()

# 모델 컴파일
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

checkpoint_cb = keras.callbacks.ModelCheckpoint('best-cnn-model.keras',
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)

# 모델 학습
history = model.fit(x_train, y_train, epochs=20, batch_size=64, validation_split=0.2,
                    callbacks=[checkpoint_cb, early_stopping_cb])

import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'val'])
plt.show()


print('\n----- 테스트 점수 -----')
print(model.evaluate(x_test, y_test))