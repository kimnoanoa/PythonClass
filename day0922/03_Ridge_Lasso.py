import pandas as pd

perch_full = pd.read_csv('./data/perch_data.csv')
print(perch_full.head())
perch_full.info() 

# 인풋 데이터 - length   height   width

import numpy as np

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = \
train_test_split(perch_full, perch_weight, random_state=42)

from sklearn.preprocessing import PolynomialFeatures

# 특성공학 적용 (디폴트 2제곱)
poly = PolynomialFeatures(include_bias=False)

poly.fit(train_input)
train_poly = poly.transform(train_input)

print('인풋 데이터 2제곱 특성공학')
print(train_poly)
print(train_poly.shape)
print(poly.get_feature_names_out())

# 테스트 데이터도 특성공학 적용
test_poly = poly.transform(test_input)

# ------------------- 스케일링 -------------------

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

# ------------------- 릿지 회귀 -------------------
# 손실함수 = MSE + L2 정규항
# 상관관계에 의해 자연적으로(수식적으로) 영향이 없는 특성은 파라미터가 작아짐

from sklearn.linear_model import Ridge

ridge = Ridge()
ridge.fit(train_scaled, train_target)
print('릿지회귀 훈련/테스트 스코어')
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))

# 최적의 규제값(alpha) 찾기
import matplotlib.pyplot as plt

train_score = []
test_score = []

alpha_list = [0.0001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    ridge = Ridge(alpha=alpha)
    ridge.fit(train_scaled, train_target)
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))

plt.plot(alpha_list, train_score, label='train')
plt.plot(alpha_list, test_score, label='test')
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()    

ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)

print('릿지회귀 규제 0.1 훈련/테스트 스코어')
print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))


# ------------------- 라쏘회귀 -------------------
# 손실함수 = MSE + L1 정규항

from sklearn.linear_model import Lasso

lasso = Lasso()
lasso.fit(train_scaled, train_target)
print('라쏘회귀 훈련 스코어')
print(lasso.score(train_scaled, train_target))
print('라쏘회귀 테스트 스코어')
print(lasso.score(test_scaled, test_target))

train_score = []
test_score = []


alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for a in alpha_list:
    lasso = Lasso(alpha=a, max_iter=10000)
    lasso.fit(train_scaled, train_target)
    train_score.append(lasso.score(train_scaled, train_target))
    test_score.append(lasso.score(test_scaled, test_target))

plt.plot(alpha_list, train_score, label='train')
plt.plot(alpha_list, test_score, label='test')
plt.xscale('log')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
plt.show()

lasso = Lasso(alpha=1)
lasso.fit(train_scaled, train_target)

print('라쏘회귀 규제 1 훈련 스코어')
print(lasso.score(train_scaled, train_target))
print('라쏘회귀 규제 1 테스트 스코어')
print(lasso.score(test_scaled, test_target))

# 0인 파라미터 개수!!!!
print(np.sum(lasso.coef_ == 0))





