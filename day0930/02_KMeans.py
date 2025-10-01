# 클러스터링 모델 KMeans

import numpy as np

# 과일사진 불러오기
fruits = np.load('./data/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

print('2d 과일 크기')  
print(fruits_2d.shape) # (300, 10000)

# KMeans 훈련
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3, init='k-means++', n_init=4, random_state=42)
km.fit(fruits_2d)

print('라벨링 결과 확인')
print(km.labels_)

print('라벨별 카운트 확인')
print(np.unique(km.labels_, return_counts=True))

# 출력 함수 정의
# 최대 10열로 맞춰서 그림 그려주는 함수 
import matplotlib.pyplot as plt

def draw_fruits(arr, ratio=1):
    n = len(arr) # n은 샘플개수
    # 한 줄에 10개씩 이미지를 그립니다. (rows=총 몇줄?)
    rows = int(np.ceil(n/10))
    # 행이 1개 이면 열 개수는 샘플개수. 그렇지 않으면 10열.
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols,
                            figsize=(cols*ratio, rows*ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()



print(fruits[km.labels_==0].shape) # 112, 100, 100

# 라벨별로 출력해보기
draw_fruits(fruits[km.labels_==0])

draw_fruits(fruits[km.labels_==1])

draw_fruits(fruits[km.labels_==2])

# KMeans가 저장해 놓은 클러스터별 평균으로 그림 그리기
draw_fruits(km.cluster_centers_.reshape(-1, 100, 100), ratio=3)

# 100번째 인덱스 사진의 클러스터 중심별 거리 뽑아보기 (유클리드 거리)
print(km.transform(fruits_2d[100:101]))

# 무슨 클러스터인지 예측하기
print(km.predict(fruits_2d[100:101]))

# 실제 무슨 과일인지 확인
draw_fruits(fruits[100:101])

# 알고리즘 반복 횟수
print(km.n_iter_)  # 4번!


'''
실제에서는 클러스터가 몇개인지 알 수 없다.
클러스터를 늘려가면서 '이너셔' 변화를 확인해 봐야 한다.
이너셔 = 데이터별로 클러스터 중심과의 거리 제곱 합
이너셔가 작아지는 속도가 줄어드는 지점이 적정 클러스터이다. (엘보우방법)
'''

# 최적의 K 찾기
inertia = []
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)

plt.plot(range(2, 7), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()



