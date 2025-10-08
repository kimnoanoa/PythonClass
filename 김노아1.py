from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import seaborn as sns

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.width', 1000)

# 1.  Seaborn의 titanic 데이터셋을 불러와 titanic 변수에 저장하시오.
print("======= 1 번 문항 =======")
titanic = sns.load_dataset('titanic')
print(titanic)
print()

# 2.  Titanic 데이터의 기본 정보를 조회하시오
print("======= 2 번 문항 =======")
print(titanic.info())
print()

# 3.  Titanic 데이터의 행과 열 개수를 조회하고, 몇 차원 배열인지 조회하시오
print("======= 3 번 문항 =======")
print("행과 열 개수 : ", titanic.shape)  
print("차원 : ", titanic.ndim)
print()  
  
# 4.  첫 3행과 마지막 2행을 조회하시오
print("======= 4 번 문항 =======")
print(titanic.head(3))
print(titanic.tail(2))
print()

# 5.  loc을 사용해 첫 5행에서 열 ['survived','pclass','sex','age']만을 가진 데이터프레임 df_loc을 만들고, 출력하시오.
print("======= 5 번 문항 =======")
df_loc = titanic.loc[:,['survived','pclass','sex','age']]
print(df_loc)
print()

# 6.  iloc을 사용해 행 10~14(포함), 열 0~3(포함)을 추출해 df_iloc에 저장하고, 출력하시오.
print("======= 6 번 문항 =======")
df_iloc = titanic.iloc[10:15,0:4]
print(df_iloc)
print()

# 7.  원본을 훼손하지 않고(inplace=False) titanic에서 열 ['deck','embark_town']을 드랍한 새 데이터프레임 df_drop_cols를 만드시오.
print("======= 7 번 문항 =======")
df_drop_cols = titanic.drop(['deck', 'embark_town'], axis=1, inplace=False)
print(df_drop_cols)
print()

# 8.  결측치가 하나라도 있는 행을 드랍한 데이터프레임 df_dropna_rows를 만드시오.
print("======= 8 번 문항 =======")
df_dropna_rows = titanic.dropna()
print(df_dropna_rows.info())
print()

# 9.  각 열별 결측치 개수를 Series로 구하시오.
print("======= 9 번 문항 =======")
missing_values = titanic.isnull().sum()
print(missing_values)
print()

# 10.  age 열의 결측치 개수만 따로 출력하시오.
print("======= 10 번 문항 =======")
missing_age = titanic['age'].isnull().sum()
print("age 열의 결측치 개수 : ", missing_age)
print()

# 11.  age 열의 평균값으로 해당 열의 결측치를 대체한 새로운 시리즈 age_filled를 만드시오(원본 불변).
print("======= 11 번 문항 =======")
age_mean = titanic['age'].mean()
age_filled = titanic['age'].fillna(age_mean)
print(age_filled)
print()

# 12.  대체 전후 age의 결측치 개수를 각각 출력하여 비교하시오.

print("======= 12 번 문항 =======")
missing_before = titanic['age'].isnull().sum() # 대체 전
age_mean = titanic['age'].mean()
age_filled = titanic['age'].fillna(age_mean) # 평균값으로 대체한 시리즈
missing_after = age_filled.isnull().sum() # 대체 후
print()
print("대체 전 age 결측치 개수 : ", missing_before)
print("대체 후 age 결측치 개수 : ", missing_after)
print()

# 13.  embarked 열의 최빈값을 describe() 결과로 확인하시오.
print("======= 13 번 문항 =======")
print(titanic['embarked'].describe())
print()

# 14.  그 최빈값으로 embarked의 결측치를 대체한 embarked_filled 시리즈를 만드시오(원본 불변).
print("======= 14 번 문항 =======")
mode_embarked = titanic['embarked'].mode()[0] # 최빈값 구하기
embarked_filled = titanic['embarked'].fillna(mode_embarked) # 결측치 대체한 새로운 시리즈 생성
# 결과 출력 (결측치 개수 확인)
print(embarked_filled.isnull().sum())  # 0 이면 결측치 대체 완료
print()

# 15.  수치형 열 중 ['age','fare']만 선택하여 0~1 범위로 Min-Max 스케일링한 데이터프레임 df_scaled를 만드시오(사전 결측 대체 필요 시 적절히 처리).
print("======= 15 번 문항 =======")
df_num = titanic[['age','fare']].copy()

df_num['age'] = df_num['age'].fillna(df_num['age'].mean())
df_num['fare'] = df_num['fare'].fillna(df_num['fare'].mean())
scaler = MinMaxScaler()
df_scaled_array = scaler.fit_transform(df_num)
df_scaled = pd.DataFrame(df_scaled_array, columns=['age', 'fare'])
print(df_scaled)
print()

# 16.  스케일링 후 각 열의 최소/최대가 0과 1에 가깝게 되었는지 describe()로 확인하시오.
print("======= 16 번 문항 =======")
print(df_scaled.describe())
print()

# 17.  age를 기준으로 아동,청소년,성인,노인 4구간으로 나누어 새 열 age_bin 을 생성하시오. 0,12,18,60,100 
print("======= 17 번 문항 =======")
print("그냥 생성만 했어요!!")
bins = [0, 12, 18, 60, 100]
labels = ['아동', '청소년', '성인', '노인']
titanic['age_bin'] = pd.cut(titanic['age'], bins=bins, labels=labels, right=False)

# 18.  각 구간별 인원수를 구하시오.
print("======= 18 번 문항 =======")
age_bin_counts = titanic['age_bin'].value_counts().sort_index()
print(age_bin_counts)
print()

# 19.  pclass와 sex로 그룹화하여 survived의 평균 생존율을 구하시오.
print("======= 19 번 문항 =======")
survival_rate = titanic.groupby(['pclass', 'sex'])['survived'].mean()
print(survival_rate)
print()

# 20.  위 결과를 생존율 내림차순으로 정렬하시오.
print("======= 20 번 문항 =======")
survival_rate_sorted = survival_rate.sort_values(ascending=False)
print(survival_rate_sorted)
print()

# 21.  age_bin(문항17)과 sex로 그룹화하여 fare의 중앙값을 구하시오.
print("======= 21 번 문항 =======")
fare_median = titanic.groupby(['age_bin', 'sex'],observed=True)['fare'].median() # 중앙값
print(fare_median)
print()

# age를 평균값으로 채우지 말고 pclass별 평균값으로 채우기
# 또는 개인적인 의견으로.. age 널 값 채우고 데이터분석 마무리
# age_mean2 = titanic['age'].mean()
# age_filled2 = titanic['age'].fillna(titanic['pclass'].map)
# print(age_filled2)

pclass_age_means = titanic.groupby('pclass')['age'].mean()

titanic['age'] = titanic['age'].fillna(titanic['pclass'].map(pclass_age_means))
print(pclass_age_means)
print()

print(titanic)

