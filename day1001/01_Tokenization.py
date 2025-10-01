sample_text = '''
    Hello! This is an example sentence for NLP preprocessing.
    Let's clean, tokenize, and get ready for modeling!
'''

import re

def clean_text(text):
    text = text.lower() # 소문자화
    text = re.sub(r'\d+', '', text) # 숫자 제거
    text = re.sub(r"[!,.']", '', text) # 특수문자 제거
    text = text.strip() # 양쪽 공백 제거
    return text

cleaned = clean_text(sample_text)
print(cleaned)

# 방법1 split()

tokens = cleaned.split()
print('----------직접 처리----------')
print(tokens)
print()

# -------------------------------------------------

# 방법 2: NLTK word_tokenize (영어 특화)
# pip install nltk

import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('punkt_tab')

tokens_nltk = word_tokenize(cleaned)

print('------------nltk 사용------------')
print(tokens_nltk)
print()

# 한국어도 해보기
text_ko = """
안녕하세요. 자연어 처리를 배우고 있어요!
저의 취미는 책을 읽는 것입니다.
여러분은 무슨 음식을 좋아하나요?
"""

print('----------nltk 사용---------')
tokens_nltk_ko = word_tokenize(text_ko)
print(tokens_nltk_ko)
print()

print('----------스플릿 사용--------')
tokens_ko_split = text_ko.split()
print(tokens_ko_split)
print()

# ----------------------------------------------------

# 방법 3: spaCy (고급분석)
# pip install spacy
# python -m spacy download en_core_web_sm
import spacy
from spacy.cli import download

nlp = spacy.load('en_core_web_sm')

doc = nlp(cleaned)

tokens_spacy = [token.text for token in doc]
print('---------spacy 사용---------')
print(tokens_spacy)
print() 
# spacy 고급분석 특징들 공부!

# 한국어도 해보기
doc2 = nlp(text_ko)
tokens_spacy_ko = [token.text for token in doc2]
print('---------spacy 사용---------')
print(tokens_spacy_ko)

#--------------------------------------------------------

# 불용어 제거
# the is at a 은 는 이가 (같은 것들 제거.)

from nltk.corpus import stopwords
# corpus - 말뭉치
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

filtered_tokens = [word for word in tokens_nltk if word not in stop_words]
print('-------- 불용어 제거 --------')
print(filtered_tokens)
print()

# 한국어 불용어 제거
korean_stopwords = [
    '의', '가', '이', '은', '는', '을', '를', '에게', '에서',
    '도', '으로', '하고', '보다', '더', '또는', '그리고', '하지만',
    '그러나', '입니다', '있습니다', '합니다', '된다'
]

filtered_tokens_ko = [word for word in tokens_nltk_ko if word not in korean_stopwords]
print('----------- 불용어 제거 한글 -----------')
print(filtered_tokens_ko)
print()
# 그러나.. 단어에 붙어있는 조사가 안없어진다..ㅠ

# ---------------------------------------------------------------

# 한국어 전처리 konlpy (한국어 특화)
# pip install konlpy

from konlpy.tag import Okt
import re


text_ko = """
1) 안녕하세요. 저는 인공지능을 공부합니다.  - 
2) 오늘은 날씨가 매우 좋네요. ㅎㅎㅎㅎㅎ  - 
3) 서울에서 맛집을 찾고 있습니다.
4) 친구와 함께 영화를 보고 카페에 갔어요. - 
5) 자연어처리는 텍스트를 이해하는 기술입니다.
6) 갑론을박 끝에 결론을 내렸다.......
7) 내일 회의는 몇 시에 시작하나요?
8) 이 제품은 품질이 우수합니다. ㅋㅋㅋㅋㅋㅋ
9) 데이터 분석은 재미있지만 어렵기도 합니다.
10) 한국어 형태소 분석을 실습해 봅시다.
"""

# 텍스트 정제 함수 (cleaning)
def clean_text(text):
    text = text.replace('\n', ' ') # 줄바꿈 -> 공백
    text = re.sub(r'\s+', ' ', text) # 여러 공백 하나로
    text = re.sub(r'\d+', '', text) # 숫자 제거
    text = re.sub(r'["()_-]', '', text) # 괄호 및 기타문자 제거
    text = re.sub(r'(.)\1+', r'\1\1', text) # 2번 이상 반복은 2번만
    text = text.strip() # 앞뒤 공백 제거
    return text

cleaned_text = clean_text(text_ko)


# Okt 객체 생성
okt = Okt()

# 토크나이징 방법별로 처리해보기
tokens_morphs = okt.morphs(cleaned_text) # 가장 작은 의미 단위인 형태소(morhpeme)
tokens_nouns = okt.nouns(cleaned_text) # 명사
tokens_pos = okt.pos(cleaned_text) # (형태소, 품사) 튜플 리스트

print('--- 정제된 텍스트 ---')
print(cleaned_text)
print()

print('--- morphs ---')
print(tokens_morphs)
print()

print('--- nouns ---')
print(tokens_nouns)
print()

print('--- pos ---')
print(tokens_pos)
print()

# 불용어 리스트
korean_stopwords = [
    '의', '가', '이', '은', '는', '을', '를', '에', '에서', '에게', '께',
    '도', '로', '으로', '과', '와', '한', '하다', '합니다', '하였다', '하는', '해서',
    '그리고', '그러나', '하지만', '또는', '및', '때문에', '그래서', '그러므로',
    '저', '저는', '나', '나는', '너', '너는', '우리', '당신', '그', '그녀', '그들',
    '이것', '저것', '그것', '거기', '여기', '저기', '곳', '데', '게', '좀',
    '뭐', '왜', '어떻게', '어디', '누구', '입니다', '있습니다', '되었습니다',
    '한다', '된다', '있다', '없다', '됐다', '됐다면', '그런데', '즉',
    '같은', '같이', '등', '때', '것', '수', '및', '중', '중에', '위해', '위한'
]

# morphs 결과에서 불용어 제거
filtered_morphs = [word for word in tokens_morphs if word not in korean_stopwords]
print('--- morphs + 불용어 제거 ---')
print(filtered_morphs)
print()

# noun 결과에서 불용어 제거
filtered_nouns = [word for word in tokens_nouns if word not in korean_stopwords]
print('--- nouns + 불용어 제거 ---')
print(filtered_nouns)
print()

# pos 결과에서 불용어 제거 (형태소만 추출)
filtered_pos = [(word, tag) for word, tag in tokens_pos if word not in korean_stopwords]
print('--- pos + 불용어 제거 ---')
print(filtered_pos)
print()


# 조사만 추출
josa = [word for word, tag in tokens_pos if tag == 'Josa']
print('조사:', josa)
print()

# 동사만 추출
verbs = [word for word, tag in tokens_pos if tag == 'Verb']
print('동사:', verbs)
print()