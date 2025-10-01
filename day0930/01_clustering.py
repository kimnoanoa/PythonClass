# 군집화 (clustering) 

import numpy as np
import matplotlib.pyplot as plt

# 과일사진 불러오기
fruits = np.load('./data/fruits_300.npy')

# 출력해보기
print('과일 전체 배열')
print(fruits)
print()

# 300, 100, 100 (100x100 짜리 300장)
print('과인 전체 shape')
print(fruits.shape)
print()

# 첫 사진의 첫 행 출력
print('첫 사진 첫 행')
print(fruits[0,0, :])
print()

# 컴퓨터는 하얀색(255) 큰 숫자를 더 비중 있다고 다룬다.
# 그래서 흑백 반전된 사진으로 저장되어 있음.
plt.imshow(fruits[0], cmap='gray')
plt.show()

# 컬러만 리버스 한 것임. (사진상 검은 부분이 255 - 헷갈림 주의)
plt.imshow(fruits[0], cmap='gray_r')
plt.show()

# 파인애플과 바나나도 뽑아보기
fig, axs = plt.subplots(1, 2)
axs[0].imshow(fruits[100], cmap='gray_r')
axs[1].imshow(fruits[200], cmap='gray_r')
plt.show()


# 과일별로 나누면서 사진마다 한 행으로 리쉐잎
apple = fruits[0:100].reshape(-1, 100*100)
pineapple = fruits[100:200].reshape(-1, 100*100)
banana = fruits[200:300].reshape(-1, 100*100)

# 100, 10000
print('사과 데이터 확인')
print(apple.shape)  

# 무슨 의미가 있을까??
print('사과 사진별로 평균 내보기')
print(apple.mean(axis=1))
print()

# 바나나가 배경(검은색)이 넓어서 대체적으로 평균이 낮음
# 과일별로 평균내서 그래프 그려보기
plt.hist(apple.mean(axis=1), alpha=0.8, label='apple')
plt.hist(pineapple.mean(axis=1), alpha=0.8, label='pineapple')
plt.hist(banana.mean(axis=1), alpha=0.8, label='banana')
plt.legend()
plt.show()

# 각 위치별로 픽셀 평균 내보기
# 바그래프로 과일별로 어디가 높은지 보자!
# 각각 10000개의 평균을 막대로 나타낸다.
# fig, axs = plt.subplots(1, 3, figsize=(20, 5))
# axs[0].bar(range(10000), apple.mean(axis=0))
# axs[1].bar(range(10000), pineapple.mean(axis=0))
# axs[2].bar(range(10000), banana.mean(axis=0))
# plt.show()

# 평균값들로 한장의 (과일별) 이미지로 만들어서 출력
apple_mean = apple.mean(axis=0).reshape(100, 100)
pineapple_mean = pineapple.mean(axis=0).reshape(100, 100)
banana_mean = banana.mean(axis=0).reshape(100, 100)

fig, axs = plt.subplots(1, 3, figsize=(20, 5))
axs[0].imshow(apple_mean, cmap='gray_r')
axs[1].imshow(pineapple_mean, cmap='gray_r')
axs[2].imshow(banana_mean, cmap='gray_r')
plt.show()

print(fruits.shape) # 300 100 100
print(apple_mean.shape) # 100 100

# 모든 그림을 '평균사과사진' 으로 빼기
# 사과 사진이라면 각각의 차이가 작죠
abs_diff = np.abs(fruits - apple_mean)
# 각각의 사진에 있는 10000개의 숫자(차이) 평균
abs_mean = np.mean(abs_diff, axis=(1,2))  
print(abs_mean.shape)

# 사과 100개의 위치별 평균을 뽑아서 '평균사과'를 만듦 (100x100)
# 300장의 과일 사진들을 각각 '평균사과' 사진 빼기를 함.
# 그러면 300장의 '(평균사과와의) 차이' 사진이 됨.
# 300장의 '차이'사진 (100x100)을 각각 평균을 냄. (10000픽셀의 평균)
# 결국 300개의 평균이 남음.
# 즉, 이 (차이)평균 숫자가 작아야 사과에 가깝다는 뜻. 

# 오차가 작은 그림 Top100 의 인덱스를 뽑아서,
# 그 인덱스를 이용, 원본 사진 불러오기.

apple_index = np.argsort(abs_mean)[:100]
apple_index = apple_index.reshape(10, 10)
fig, axs = plt.subplots(10, 10, figsize=(10,10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[apple_index[i, j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()

# 파인애플이랑 바나나도 100개 뽑아보기.
