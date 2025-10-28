# ----- 손실곡선 그려보기 -----

import keras
import tensorflow as tf

keras.utils.set_random_seed(42) # 케라스와 관련된 난수 시드 고정
tf.random.set_seed(42) # 텐서 연산 내부에서 사용하는 시드 고정
tf.config.experimental.enable_op_determinism() # 텐서플로 내부 연산에서 가능한 동일한 결과

from sklearn.model_selection import train_test_split

print('\n----- 데이터 로드 -----')
(train_input, train_target), (test_input, test_target) = \
    keras.datasets.fashion_mnist.load_data()

print('\n----- 데이터 스케일링 -----')
train_scaled = train_input / 255.0

print('\n----- 훈련/테스트셋 분할 -----')
train_scaled, val_scaled, train_target, val_target = train_test_split(
    train_scaled, train_target, test_size=0.2, random_state=42)


# 모델 생성 함수
def model_fn(a_layer=None):  # 매개변수 디폴트값 None
    model = keras.Sequential()
    model.add(keras.layers.Input(shape=(28,28)))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(100, activation='relu'))
    if a_layer:
        model.add(a_layer)
    model.add(keras.layers.Dense(10, activation='softmax'))
    return model

# 함수를 톤해 모델 생성
model = model_fn()
print()
model.summary()

# 모델 컴파일 및 훈련
# 이번에는 model.fit 을 history에 담는다. (모델 훈련 내용 담기)
model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print('\n----- 모델 훈련 -----')
history = model.fit(train_scaled, train_target, epochs=5, verbose=1)

# history 객체에 훈련 측정값이 딕셔너리로 담겨있다.
print('\n----- history key 값 확인 -----')
print(history.history.keys()) # dict_keys(['accuracy', 'loss'])

print('\n----- 에포크별 로스값 -----')
print(history.history['loss'])

print('\n----- 에포크별 정확도 -----')
print(history.history['accuracy'])

import matplotlib.pyplot as plt

# 에포크별 로스값 그래프
plt.plot(history.history['loss']) # 에포크별 로스
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

# 에포크별 정확도 그래프 출력
plt.plot(history.history['accuracy'])
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()

# # 에포크를 20으로 늘려보기
# model = model_fn() # 옵티마이저 디폴트 RMSProp?
# model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# print('\n----- 모델훈련 (에포크 20) -----')
# history = model.fit(train_scaled, train_target, epochs=20)

# plt.plot(history.history['loss'])
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.show()

# 과연 로스 값이 낮으면 무조건 좋은걸까?
# 검증세트 돌려서 과대적합 과소적합 확인해 봐야 한다.

# ---------- 검증 손실 ----------

# # 검증데이터 추가해서 훈련
# model = model_fn()
# model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# print('\n----- 모델훈련 (검증 데이터 추가) -----')
# history = model.fit(train_scaled, train_target, epochs=20,
#                     validation_data=(val_scaled, val_target))

# print('\n----- history key 값 확인 (검증 추가) -----')
# print(history.history.keys())
# # dict_keys(['accuracy', 'loss', 'val_accuracy', 'val_loss'])

# # 훈련/검증 로스 그래프 출력
# plt.plot(history.history['loss'], label='train')
# plt.plot(history.history['val_loss'], label='val')
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend()
# plt.show()

# 에포크 20 결론은 과대적합! 

# adam 으로 과대적합이 해결 될까?
# model = model_fn()
# optimizer = keras.optimizers.Adam(learning_rate=0.001) # 옵티마이저 세팅
# model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# print('\n----- 모델훈련 adam -----')
# history = model.fit(train_scaled, train_target, epochs=20,
#                     validation_data=(val_scaled, val_target))

# plt.plot(history.history['loss'], label='train')
# plt.plot(history.history['val_loss'], label='val')
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend()
# plt.show()

# 많이 나아지진 않았다.

# ---------- 드롭아웃 ----------

# 뉴런을 랜덤하게 꺼버린다 - 일반화 성능 향상 (마치 여러 모델을 앙상블한 효과)
# 드롭아웃 층 추가해서 모델생성
# model = model_fn(keras.layers.Dropout(0.3))
# print()
# model.summary()

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# print('\n----- 모델훈련 (dropout 추가) -----')
# history = model.fit(train_scaled, train_target, epochs=20,
#                     validation_data=(val_scaled, val_target))

# plt.plot(history.history['loss'], label='train')
# plt.plot(history.history['val_loss'], label='val')
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.legend()
# plt.show()

# 성능 향상 (과대적합 완화)
# 11번째 에포크가 적절해 보인다.

# ---------- 모델 저장과 복원 (에포크 11)-----------

model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print('\n----- 모델훈련 (에포크 11) -----')
history = model.fit(train_scaled, train_target, epochs=11,
                    validation_data=(val_scaled, val_target))

# 모델 구조와 파라미터를 함께 저장하는 방법
model.save('model-whole.keras')

# 파라미터만 저장하는 방법
model.save_weights('model.weights.h5')

# 실험1 - 새로운 모델을 반들어서 파라미터 이식하기
# 구조가 정확히 같아야 한다. 
model = model_fn(keras.layers.Dropout(0.3))
model.load_weights('model.weights.h5')


# 학습을 한 모델이 아니어서 evaluate() 함수를 쓸 수 없다..
# 그래서 아래와 같이 진행..
import numpy as np

print('\n----- 예측값 결과 -----')
print(model.predict(val_scaled))

# 10개의 확률값 중에 가장 큰 값의 인덱스 반환
val_labels = np.argmax(model.predict(val_scaled), axis=-1)

print('\n----- 정답과 비교하여 정확도 계산 -----')
print(np.mean(val_labels == val_target))
# ex) 1 1 0 0 1 0 1 0 0 0 0 1 1 1 ..... 의 평균 값

'''
컴파일 하고 훈련해서 evaluate 사용해도 된다!
model.compile(optimizer='adam', loss....)...
'''

# 실험2 - 모델 전체를 불러오기
model = keras.models.load_model('model-whole.keras')
# 이미 컴파일이 되어있기 때문에 evaluate 가능
print('\n----- evaluate 값 -----')
model.evaluate(val_scaled, val_target)

# ---------- 콜백 ----------

# model = model_fn(keras.layers.Dropout(0.3))
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# # ModelCheckpoint - 에포크마다 모델을 저장 (계속 덮어씌움)
# # save_best_only=True - best 모델을 파일로저장 (이전것 보다 안 좋으면 안 덮어씌움)

# checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.keras',
#                                                 save_best_only=True)

# print('\n----- 모델훈련 (베스트 모델 저장) -----')
# model.fit(train_scaled, train_target, epochs=20,
#           validation_data=(val_scaled, val_target),
#           callbacks=[checkpoint_cb])
# # 베스트 모델 선정 디폴트 = 검증 로스 가장 낮은 모델

# # 위에서 저장된 베스트 모델을 로드하여 evaluate 해보자
# model = keras.models.load_model('best-model.keras')
# print('\n----- 베스트 모델 evaluate -----')
# model.evaluate(val_scaled, val_target)

# ------------------------------------------------------

# 20 에포크 동안 할 필요가 없다.
# patience=2 >> 2번 연속 검증 점수가 향상되지 않으면 훈련 종료
# restore_best_weights=True >> 훈련중 가장 낮은 검증손실을 낸 모델 파라미터로 되돌림.

model = model_fn(keras.layers.Dropout(0.3))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
checkpoint_cb = keras.callbacks.ModelCheckpoint('best-model.keras',
                                                save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2,
                                                  restore_best_weights=True)

print('\n----- 모델훈련 (콜백 2개) -----')
history = model.fit(train_scaled, train_target, epochs=20,
                    validation_data=(val_scaled, val_target),
                    callbacks=[checkpoint_cb, early_stopping_cb]) 

# 몇 에포크에서 멈췄는지 출력
# 출력값 +1 -2 = 베스트 모델
print('\n----- 멈춘 에포크 시점 -----')
print(early_stopping_cb.stopped_epoch) # 9 >>>>  9 -1 +2 = 8 (베스트 에포크)

plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
plt.show()

print('\n----- 베스트 모델 evaluate -----')
model.evaluate(val_scaled, val_target)