
# 도미 데이터
bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 방어 데이터
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(smelt_length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_data = [[l, w] for l, w in zip(length, weight)]

# 인풋 데이터
print(fish_data)
print()

# 타겟 데이터 (정답지)
# 1 방어 / 0 도미
fish_target = [1]*35 + [0]*14
print(fish_target)
print()

# k-최근접 이웃 알고리즘 학습
# KNN (K-Nearest Neighbors)
# K - 근처 몇개의 이웃을 참고하지 (K 개)
from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()

# KNN 분류 학습
kn.fit(fish_data, fish_target)
print('kn 모델변수에 학습 완료')
print()

# 방어와 도미 그래프
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.scatter(30, 600, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print('예측 결과')
print(kn.predict([[30, 600]]))
print()


# KNN - 모든 점의 거리를 다 계산해서 가장 가까운 5개의 이웃을 보고 분류 
# 모든 데이터의 정보를 가지고 있음
# 사실상 훈련이라고 하기엔 모호함.

print(kn._fit_X)
print()

print(kn._y)
print()


# KNN 분류 작동 - 가장 가까운 이웃 K개를 조사하여 (뭐가 많은지) 분류
# 디폴트 이웃수(K) 5개
# K를 49개로 바꿔 보면??

kn49 = KNeighborsClassifier(n_neighbors=49)

kn49.fit(fish_data, fish_target)

# 분류 모델에서 score는 맞춘수/전체
print(kn49.score(fish_data, fish_target))
print(35/49)
print()

print('아무 생선 3마리 예측 시켜보기')
print(kn49.predict([[30, 600], [20, 100], [15, 70]]))
print()

# 학습 데이터 준비 (인풋데이터, 타겟데이터)
# 모델 선정 및 불러오기
# 데이터로 모델 학습
# 스코어 확인 / 특정 데이터 예측
# (그래프로 확인)


# 5개부터 시작해서 스코어 확인
# 과연 몇일때 스코어가 1미만이 될까? 알아내세요

kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
# kn 안에 생선 데이터만 저장 완료

for n in range(5, 50):
    kn.n_neighbors = n

    score = kn.score(fish_data, fish_target)

    if score < 1:
        print(n, '일때', score)
        break