from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, classification_report
from scipy.sparse import hstack

print('임포트 완료')
print()

remove_parts = ('headers', 'footers', 'quotes')
train = fetch_20newsgroups(subset='train', remove=remove_parts)
test = fetch_20newsgroups(subset='test', remove=remove_parts)
print('데이터 로드 완료')

X_train_text = train.data
y_train = train.target
X_test_text = test.data
y_test = test.target
target_names = train.target_names
print('데이터 분할 완료')
print('데이터 개수 / 클래스 개수')
print(f'Train: {len(X_train_text)} / Test: {len(X_test_text)} \
      / Classes: {len(target_names)}')

# 벡터화 정말 재밌다

word_vec = TfidfVectorizer(
    analyzer='word', # 디폴트값, 토큰 단위가 단어이다
    ngram_range=(1, 2), 
    min_df=3, # 문서에서 3회 미만이면 제거
    max_df=0.97, # 문서에서 97% 이상 등장하면 제거
    lowercase=True,
)
print('단어 벡터화 시작 n-gram(1,2)')
Xw_train = word_vec.fit_transform(X_train_text)
Xw_test = word_vec.transform(X_test_text)
print('단어 벡터화 끝')



# 문자 벡터화
char_vec = TfidfVectorizer(
    analyzer='char_wb', # 토큰 단위가 문자
    ngram_range=(3, 5),
    min_df=3,
    lowercase=True
)
print('문자 벡터화 시작 n-gram(3,5)')
Xc_train = char_vec.fit_transform(X_train_text)
Xc_test = char_vec.transform(X_test_text)
print('문자 벡터화 끝')

'''
희소행렬, COO, CSR
'''

X_train = hstack([Xw_train, Xc_train]).tocsr()
X_test = hstack([Xw_test, Xc_test]).tocsr()

print('최종 데이터 크기 (훈련 / 테스트)')
print('Shapes:', X_train.shape, X_test.shape)

# 모델 세팅
clf = LogisticRegression(
    penalty='l2',
    C=2.0,
    solver='saga', # 대규모 희소행렬에 특화
    max_iter=2000,
    n_jobs=-1
)
'''
모델마다 옵션을 꼭 추가 공부해보세요.
'''
import time
start_time = time.time()
print('모델 학습 시작')
clf.fit(X_train, y_train)
print('모델 학습 끝')
end_time = time.time()
learning_time = end_time - start_time
print(f'총 학습 시간: {learning_time:.2f}초')
print()

# 평가
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
macro_f1 = f1_score(y_test, y_pred, average='macro')

print('=== Test Metrics ===')
print(f'Accuracy : {acc:.4f}')
print(f'Macro F1 : {macro_f1:.4f}')

print('=== Classification Report (요약) ===')
print(classification_report(y_test, y_pred, 
                            target_names=target_names, digits=4))

# 샘플예측
samples = [
    "The new graphics card supports OpenGL and has great performance.",
    "The government policy on healthcare has sparked intense debate.",
    "I love riding my motorcycle during the summer road trips."
]

sample_Xw = word_vec.transform(samples)
sample_Xc = char_vec.transform(samples)
sample_X = hstack([sample_Xw, sample_Xc]).tocsr()

sample_pred = clf.predict(sample_X)

print(sample_pred)
for i in sample_pred:
    print(target_names[i])