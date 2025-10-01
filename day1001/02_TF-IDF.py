import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

corpus = [
    "I love natural language processing and machine learning.",
    "Natural language processing is a subfield of artificial intelligence.",
    "Machine learning enables computers to learn from data.",
    "Deep learning is a type of machine learning.",
    "I love deep learning and NLP!"
]

# 전처리

import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r"[!,.']", '', text)
    return text

cleaned_corpus = [clean_text(doc) for doc in corpus]
print(cleaned_corpus)

# TfidfVectorizer 사용
# TF (Term Frequency): 한 문장 안에 단어가 몇 번 나왔는지
# IDF (Inverse Document Frequency): 전체 문장에 얼마나 드물게 나왔는지

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(cleaned_corpus)

print(type(tfidf_matrix))
print(tfidf_matrix)
print()

# 단어사전 확인
print('단어사전')
print(vectorizer.vocabulary_)
print()

# -------------------------------------------------

import pandas as pd

df_tfidf = pd.DataFrame(tfidf_matrix.toarray(), 
                        columns=vectorizer.get_feature_names_out())
print(df_tfidf)
print()