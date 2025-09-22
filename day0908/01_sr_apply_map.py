# 시리즈 원소에 함수 매핑

# seaborn과 pandas 라이브러리 불러오기
import seaborn as sns
import pandas as pd

# seaborn에 내장된 'titanic' 데이터셋을 불러옴
titanic = sns.load_dataset('titanic')

# 'age'와 'fare' 열만 선택해서 새로운 데이터프레임(df) 생성
df = titanic.loc[:, ['age', 'fare']]

# df의 처음 5행 출력 (age와 fare만 보임)
print(df.head())
print()

# 사용자 정의 함수 - 입력값(n)에 10을 더해서 반환
def add_10(n):
    return n + 10

# 사용자 정의 함수 - 두 값을 더해서 반환
def add_two_obj(a, b):
    return a + b

# add_10 함수 테스트 (10 + 10 = 20)
print(add_10(10))

# add_two_obj 함수 테스트 (10 + 10 = 20)
print(add_two_obj(10, 10))

# 시리즈 'age'의 각 원소에 add_10 함수를 적용
# 즉, 모든 나이에 10을 더한 결과를 sr1에 저장
sr1 = df['age'].apply(add_10)

# 결과 확인 (결측값 NaN은 그대로 유지됨)
print(sr1.head())
print()

# 위와 같은 동작을 lambda(익명 함수)로도 처리 가능
# n에 10을 더하는 함수를 직접 정의해서 apply에 전달
sr2 = df['age'].apply(lambda n: n + 10)

# 결과 확인
print(sr2.head())
print()

# add_two_obj 함수 사용 - age 열의 각 값(a)에 10(b)을 더함
# 여기서 b=10은 고정값으로 전달됨 (apply에 인자로 넘김)
sr3 = df['age'].apply(add_two_obj, b=10)

# 결과 확인
print(sr3.head())
print()

# 동일한 동작을 lambda 함수로 구현 (a + b), b=10 전달
sr4 = df['age'].apply(lambda a, b: a + b, b=10)

# 결과 확인
print(sr4.head())
print()

# map 함수 사용 - age 값이 30보다 큰지 확인하는 함수 정의
def over_thirty(age):
    return age > 30

# map을 이용해 age 값이 30 초과인지 여부를 불리언 값으로 반환
# NaN 값은 그대로 유지
sr_map = df['age'].map(over_thirty)

# 결과 확인 (True/False가 출력됨)
print(sr_map.head())
print()

# 위와 동일한 작업을 lambda 함수로 수행
# 30보다 크면 True, 아니면 False 반환
sr_map2 = df['age'].map(lambda age: True if age > 30 else False)

# 결과 확인
print(sr_map2.head())
print()

# 성별 값에 어떤 값들이 있는지 확인 ('male', 'female')
print(titanic['sex'].unique())
print()

# 성별 컬럼의 앞쪽 데이터 확인
print(titanic['sex'].head())
print()

# 성별을 숫자로 매핑하기 위한 딕셔너리 정의
# male → 0, female → 1
gender_dict = {'male': 0, 'female': 1}

# map을 사용해 성별 텍스트 값을 숫자로 변환해서 'gender'라는 새 컬럼에 저장
titanic['gender'] = titanic['sex'].map(gender_dict)

# 데이터프레임 정보 출력 (새 컬럼 'gender'가 추가된 것 확인 가능)
titanic.info()
print()

# 전체 데이터프레임 중 처음 5행 출력 (gender 열 포함)
print(titanic.head())
print()
