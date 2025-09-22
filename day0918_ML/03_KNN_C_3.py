fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

import numpy as np

# 넘피 컬럼스택 (리스트들 튜플로 전달)
print(np.column_stack(([1,2,3], [4,5,6])))
print()

# 도미/방어의  무게/길이  묶어주기
fish_data = np.column_stack((fish_length, fish_weight))
print(fish_data[:5])
print()

# 넘피 배열 만들기 (넘피 맛보기)
print(np.ones(5))
print(np.zeros(5))
print(np.full(5, 2))
print(np.full((3,3), 7))

fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)
print()

from sklearn.model_selection import train_test_split

# 알아서 섞어준다.
# 디폴트 비율 75:25
train_input, test_input, train_target, test_target = train_test_split(
    fish_data, fish_target, test_size=0.25, random_state=42)

print(train_input.shape, test_input.shape)
print()

print(train_target.shape, test_target.shape)
print()

print(test_target)
print()

# 훈련
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier()
kn.fit(train_input, train_target)

print('-----훈련 스코어-----')
print(kn.score(test_input, test_target))
print()


# 25, 150 월척!

import matplotlib.pyplot as plt

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print('-----월척의 종류는???-----')
print(kn.predict([[25, 150]]))
print()

distances, indexes = kn.kneighbors([[25, 150]])
print('근처 이웃 인덱스', indexes)
print()

# 근처 이웃들 확인해보자
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()


# x축 늘려서 산점도 압축시키기
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25, 150, marker='^')
plt.scatter(train_input[indexes,0], train_input[indexes,1], marker='D')
plt.xlim((0, 1000))
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 스케일링 (표준화)
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

print("평균: ", mean)
print("표준편차: ", std)

train_scaled = (train_input - mean) / std

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(25, 150, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 월척도 스케일링 해주자!!
new = ([25, 150] - mean) / std

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 다시 훈련
kn.fit(train_scaled, train_target)

# 중요! (트레인 평균,표준편차로!!) 테스트 데이터도 스케일링 
test_scaled = (test_input - mean) / std

print('스코어: ', kn.score(test_scaled, test_target))
print('월척은? : ', kn.predict([new]))

distances, indexes = kn.kneighbors([new])

# 이웃들 다시 확인해 보자.
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1], marker='^')
plt.scatter(train_scaled[indexes,0], train_scaled[indexes,1], marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print('이웃들 거리를 확인해보자')
print(distances)


