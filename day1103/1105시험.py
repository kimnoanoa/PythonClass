# IMDB 영화 리뷰 감성분석 (LSTM 기반)
# 작성자: 김노아

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# 1. 데이터 준비
print("IMDB 데이터셋 불러오는 중...")

# IMDB 데이터셋은 Keras에서 기본 제공하는 영화 리뷰 감성 분석용 데이터입니다.
# 각 리뷰는 이미 정수 인덱스로 변환된 형태로 제공됩니다.
# label: 0 → 부정적인 리뷰, 1 → 긍정적인 리뷰
# num_words: 상위 10,000개의 자주 등장하는 단어만 사용하여 희소 단어는 제거합니다.
num_words = 10000   
maxlen = 200        # 각 리뷰의 최대 단어 수를 200으로 제한 (패딩 기준)

# 훈련용(25,000개), 테스트용(25,000개) 데이터셋 로드
(x_train, y_train), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=num_words)

print(f"훈련 데이터 개수: {len(x_train)}, 테스트 데이터 개수: {len(x_test)}")

# 2. 데이터 전처리 (시퀀스 패딩)
print("시퀀스 패딩 처리 중... (길이를 동일하게 맞춤)")

# 각 리뷰는 단어의 개수가 제각각이므로,
# 신경망이 일정한 입력 길이를 받을 수 있도록 모든 리뷰 길이를 동일하게 맞춥니다.
# maxlen보다 짧은 리뷰는 0으로 채우고, 긴 리뷰는 잘라냅니다.
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = keras.preprocessing.sequence.pad_sequences(x_test, maxlen=maxlen)

print("훈련 데이터 형태:", x_train.shape)
print("테스트 데이터 형태:", x_test.shape)

# 3. 모델 구성
print("LSTM 모델 구성 중...")

# Sequential 모델: 층을 순차적으로 쌓는 단순한 구조
model = keras.Sequential([
    # (1) Embedding 층:
    # 단어 인덱스를 밀집 벡터(dense vector)로 변환하여 의미 공간에 매핑.
    # input_dim=10000 → 단어 사전 크기
    # output_dim=128 → 각 단어를 128차원 벡터로 표현
    # input_length=maxlen → 각 입력 시퀀스의 길이
    layers.Embedding(input_dim=num_words, output_dim=128, input_length=maxlen),

    # (2) LSTM 층:
    # 시퀀스(문장 내 단어 순서) 정보를 학습하기 위한 순환신경망(RNN) 구조.
    # dropout → 입력에 대한 드롭아웃 비율
    # recurrent_dropout → 순환 상태에 대한 드롭아웃 비율
    layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2),

    # (3) Dropout 층:
    # LSTM 층의 출력을 일부 무작위로 끊어 과적합(overfitting)을 방지.
    layers.Dropout(0.3),

    # (4) 출력층(Dense):
    # sigmoid 활성화 함수를 사용해 0~1 사이의 확률값으로 긍정/부정 예측.
    layers.Dense(1, activation='sigmoid')
])

# 4. 모델 설정 (컴파일)
print("모델 컴파일 중...")

# 모델 학습을 위한 손실함수, 최적화 알고리즘, 평가 지표 설정
model.compile(
    optimizer='adam',                 # Adam: 효율적인 가중치 최적화 알고리즘
    loss='binary_crossentropy',       # 감성 분류는 이진 분류이므로 binary_crossentropy 사용
    metrics=['accuracy']              # 모델의 정확도를 모니터링
)

# 5. 콜백 설정 (모델 저장, 조기 종료)
print("콜백 설정 중...")

# ModelCheckpoint: 검증 손실(val_loss)이 가장 낮을 때의 모델을 자동 저장
checkpoint_cb = keras.callbacks.ModelCheckpoint(
    filepath="best_lstm_model.h5",    # 저장 파일명
    monitor='val_loss',               # 기준: 검증 손실
    save_best_only=True,              # 가장 좋은 성능일 때만 저장
    verbose=1
)

# EarlyStopping: 일정 횟수(epoch) 동안 검증 성능이 개선되지 않으면 학습을 중단
earlystop_cb = keras.callbacks.EarlyStopping(
    monitor='val_loss',               # 기준: 검증 손실
    patience=3,                       # 3번 연속 개선되지 않으면 중단
    restore_best_weights=True,        # 가장 성능 좋았던 시점의 가중치 복원
    verbose=1
)

# 6. 모델 학습
print("\n모델 학습 시작\n")

# validation_split=0.2 → 훈련 데이터의 20%를 검증용으로 자동 분리
# callbacks → 위에서 정의한 모델 저장, 조기 종료 기능 적용
history = model.fit(
    x_train, y_train,
    epochs=10,
    batch_size=128,
    validation_split=0.2,
    callbacks=[checkpoint_cb, earlystop_cb],
    verbose=1
)

print("\n학습 완료!")

# 7. 학습 결과 시각화
print("학습 결과 그래프 출력 중...")

plt.figure(figsize=(10, 5))

# (1) 손실(Loss) 변화 그래프
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# (2) 정확도(Accuracy) 변화 그래프
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

# 8. 테스트 데이터 평가
print("\n테스트셋 평가 중...")

# 학습된 모델을 사용하여 테스트 데이터의 성능 평가
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)

print(f"\n테스트 정확도: {test_acc:.4f}")   # 테스트 정확도 출력
print(f"테스트 손실: {test_loss:.4f}")      # 테스트 손실 출력

print("\n전체 과정이 완료되었습니다.")
