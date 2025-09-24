# 결정트리 - 의사 결정 나무

import pandas as pd

wine = pd.read_csv('https://bit.ly/wine_csv_data')

print(wine.head())
wine.info()
print()
print(wine.describe())
print()

data = wine[['alcohol', 'sugar', 'pH']]
target = wine['class']
print(target.unique())
print()

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    data, target, test_size=0.2, random_state=42)

print(train_input.shape, test_input.shape)
print()

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_scaled, train_target)

print('로지스틱 리그레션 훈련/테스트 스코어')
print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))
print('파라미터 결과')
print(lr.coef_, lr.intercept_)
print()

# ---------- 결정 트리 ----------

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)

print('결정트리 훈련/테스트 스코어')
print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled, test_target))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(10,7))
plot_tree(dt)
plt.show()

plt.figure(figsize=(10,7))
plot_tree(dt, max_depth=1, filled=True,
          feature_names=['alcohol', 'sugar', 'pH'])
plt.show()


# 트리 깊이를 3으로 제한하기
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_scaled, train_target)

print('깊이 3 나무 스코어')
print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled, test_target))

plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()

# 사실은 (in fact) (the truth is...) 스케일링 안해도 된다.
dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(train_input, train_target)

print('노 스케일링 스코어')
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

# 특성별로 중요도 뽑아보기
print('----- 특성별 중요도 -----')
print(dt.feature_importances_)

# 정보이득이 0.0005 보다 적으면 더이상 분할 하지 마라...
dt = DecisionTreeClassifier(min_impurity_decrease=0.0005, random_state=42)
dt.fit(train_input, train_target)

print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol', 'sugar', 'pH'])
plt.show()

# -----------------------------------------

fish = pd.read_csv('https://bit.ly/fish_csv_data')
print(fish.head())
print()

# 물고기 종류 확인 (7개)
print(pd.unique(fish['Species']))
print()

# 인풋 데이터
fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']]

print(fish_input.head())
print()

# 타겟 데이터
fish_target = fish['Species']

# 훈련/테스트 셋 분리 (디폴트 몇대몇? 75:25)
from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state=42)

dt = DecisionTreeClassifier(max_depth=50, random_state=42)
dt.fit(train_input, train_target)

print('다중분류 스코어')
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

# plt.figure(figsize=(20,15))
# plot_tree(dt, filled=True, feature_names=['Weight', 'Length', 'Diagonal', 'Height', 'Width'])
# plt.show()