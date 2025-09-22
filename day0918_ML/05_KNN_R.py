import numpy as np

perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

import matplotlib.pyplot as plt

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 저번시간 - 길이와 무게로 종류 분류
# 길이로 무게(숫자) 예측하기

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)

# 인풋 데이터 모양 확인 (2차원이어야 한다.)
print(train_input.shape, test_input.shape)

# 넘파이 기능 맛보기
test_array = np.array([1, 2, 3, 4])
print(test_array.shape)

test_array = test_array.reshape(2, 2)
print(test_array.shape)

# 곱하기 숫자 맞춰서 바꿔 줘야 한다.
# test_array = test_array.reshape(3, 2)
# print(test_array.shape)

print('모양 바꾸기 전')
print(train_input)

# -1로 적어주면 알아서 계산해 준다!
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)

print('모양 바꾸기 후')
print(train_input)

print(train_input.shape, test_input.shape)


# 최근접 이웃 회귀
from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor() # 주변 데이터(k개의 이웃)를 기반으로 예측.
# k-최근접 이웃 회귀 모델 훈련!
knr.fit(train_input, train_target)

print('knr 테스트 스코어')
print(knr.score(test_input, test_target))
print() # 0.992809406101064 테스트


print('knr 트레인 스코어')
print(knr.score(train_input, train_target))
print() # 0.9698823289099254 트레인

# 트레인셋이 테스트셋보다 낮다. (과소 적합)
# 훈련만 너무 높다 (과대 적합)
# 둘 다 너무 낮다 (과소 적합)
# 훈련세트가 적당히 높아야 정상.

knr.n_neighbors = 3

# 모델을 다시 훈련
knr.fit(train_input, train_target)
print('3이웃 - 트레인/테스트 스코어')
print(knr.score(train_input, train_target))
print(knr.score(test_input, test_target))

print('예측 결과')
print(knr.predict(test_input))

# 이웃수를 1,5,10 늘려보면서
# 모델이 단순해지는 것을 그래프로 관찰하기

knr = KNeighborsRegressor()

x = np.arange(5,45).reshape(-1,1)

for n in [1,5,10]:
    # 모델 훈련
    knr.n_neighbors = n
    knr.fit(train_input,train_target) # 훈련 완료
    # 5~45 까지 넣어가며 예측
    prediction = knr.predict(x)
    
    # 원래 데이터 산점도
    plt.scatter(train_input,train_target)
    # 5~45 넣은 예측값 선그래프
    plt.plot(x,prediction,color='red')
    plt.title(f'n_neighbors = {n}')
    plt.xlabel('length')
    plt.ylabel('weight')
    plt.show()
    
    
    
