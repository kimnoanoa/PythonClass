# PCA (Principal Component Analysis)

import numpy as np

# 과일사진 불러오기
fruits = np.load('./data/fruits_300.npy')
fruits_2d = fruits.reshape(-1, 100*100)

# 주성분 분석
# 2차원 데이터를 기대
# 사진인지 아닌지 상관 없음.

from sklearn.decomposition import PCA

pca = PCA(n_components=50)
pca.fit(fruits_2d)

# 주성분 모양 50, 10000
print(pca.components_.shape)

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

print('주성분 뽑아보기')
print(pca.components_)

# 주성분 그려보기
draw_fruits(pca.components_.reshape(-1, 100, 100))

print('원본 배열 크기')
print(fruits_2d.shape) # 300, 10000

# 주성분으로 차원 축소
fruits_pca = pca.transform(fruits_2d)

print('차원 축소 후 크기')
print(fruits_pca.shape) # 300, 50
print('첫번째 요소')
print(fruits_pca[0]) # 픽셀이 아니다.

# 다시 복원해서 그려보기
fruits_inverse = pca.inverse_transform(fruits_pca)
print('복원 후 크기 - 원본 비슷하게')
print(fruits_inverse.shape)

fruits_reconstruct = fruits_inverse.reshape(-1, 100, 100)

for start in [0, 100, 200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print()

# (설명된 분산) 50개의 주성분이 원본을 얼마나 잘 표현 했을까?
print('주성분별 설명 퍼센티지')
print(pca.explained_variance_ratio_)
print('50성분이 원본을 얼마나 표현했나?')
print(np.sum(pca.explained_variance_ratio_)) # 92%


# 주성분 Top10 이면
plt.plot(pca.explained_variance_ratio_)
plt.show()

# ===================================================

# 차원을 축소해서 분류 시키기 (로지스틱 리그레션 - 지도학습)
# 원본 그대로 분류 시키기 
# 두 개를 비교 (누가 더 빠른가. 스코어는 어떤가?)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

target = np.array([0] * 100)




# 주성분 2개로 축소해서 -> kmeans 나누고 -> 2차원에 그려보기
