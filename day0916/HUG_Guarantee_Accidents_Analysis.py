import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 보기 설정
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 300)

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_prop = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_prop)
plt.rcParams['axes.unicode_minus'] = False

# 파일 경로
filePath_detail = "data\주택도시보증공사_전세보증금반환보증 상세현황_20250630.csv"
filePath_accident = "data\\주택도시보증공사_보증사고현황_20231231.csv"

# CSV 파일 로딩
df_detail = pd.read_csv(filePath_detail, encoding='cp949')
df_accident = pd.read_csv(filePath_accident, encoding='cp949')

print(df_accident)
print(df_detail)
print("df_detail 컬럼명 목록:")
print(df_detail.columns.tolist())

# 함수 정의
def clean_columns(df):
    df.columns = (
        df.columns.str.strip()           # 앞뒤 공백 제거
        .str.replace(" ", "_")           # 중간 공백도 밑줄로
        .str.replace("(", "")
        .str.replace(")", "")
        .str.replace("억원", "(억)")
    )
    return df


#  여기에서 꼭 호출해야 함
df_detail = clean_columns(df_detail)
df_accident = clean_columns(df_accident)

# 지역명 통일 작업
df_detail['지역'] = df_detail['지역'].str.replace('서울특별시', '서울')
df_detail['지역'] = df_detail['지역'].str.replace('인천광역시', '인천')
df_detail['지역'] = df_detail['지역'].str.replace('경기도', '경기')
df_detail['지역'] = df_detail['지역'].str.replace('부산광역시', '부산')
df_detail['지역'] = df_detail['지역'].str.replace('대구광역시', '대구')
df_detail['지역'] = df_detail['지역'].str.replace('광주광역시', '광주')
df_detail['지역'] = df_detail['지역'].str.replace('경북', '경상북도')
df_detail['지역'] = df_detail['지역'].str.replace('경남', '경상남도')
df_detail['지역'] = df_detail['지역'].str.replace('충북', '충청북도')
df_detail['지역'] = df_detail['지역'].str.replace('충남', '충청남도')
df_detail['지역'] = df_detail['지역'].str.replace('전남', '전라남도')
df_detail['지역'] = df_detail['지역'].str.replace('전북', '전라북도')
df_detail['지역'] = df_detail['지역'].str.replace('강원도', '강원')
df_detail['지역'] = df_detail['지역'].str.replace('대전광역시', '대전')
df_detail['지역'] = df_detail['지역'].str.replace('울산광역시', '울산')
df_detail['지역'] = df_detail['지역'].str.replace('세종특별자치시', '세종')
df_detail['지역'] = df_detail['지역'].str.replace('제주특별자치도', '제주')


# 다시 확인
print("정리된 df_detail 컬럼명 목록:")
print(df_detail.columns.tolist())
print(df_accident.columns.tolist())

# ------ 결측치 처리 ------
# 결측치 현황 확인
print("df_detail 결측치:")
print(df_detail.isnull().sum())

print("df_accident 결측치:")
print(df_accident.isnull().sum())
print()

# 숫자형 컬럼 결측치 → 0으로 대체
df_detail['건수'] = pd.to_numeric(df_detail['건수'], errors='coerce').fillna(0).astype(int)
df_detail['보증금액'] = pd.to_numeric(df_detail['보증금액'], errors='coerce').fillna(0).astype(int)

df_accident['건수'] = pd.to_numeric(df_accident['건수'], errors='coerce').fillna(0).astype(int)
df_accident['금액(억)'] = pd.to_numeric(df_accident['금액(억)'], errors='coerce').fillna(0).astype(float)

# ------ 이상치 제거 ------

# 건수, 금액이 음수인 경우 제거
df_detail = df_detail[(df_detail['건수'] >= 0) & (df_detail['보증금액'] >= 0)]
df_accident = df_accident[df_accident['건수'] >= 0]

# 발급년도 및 월 범위 확인
df_detail = df_detail[(df_detail['발급년도'] >= 2000) & (df_detail['발급년도'] <= 2030)]
df_detail = df_detail[(df_detail['월'] >= 1) & (df_detail['월'] <= 12)]

df_detail_original = df_detail.copy()
df_accident_original = df_accident.copy()

# 이상치 제거 코드 실행

print("df_detail 이상치 제거로 사라진 행 수:", len(df_detail_original) - len(df_detail))
print("df_accident 이상치 제거로 사라진 행 수:", len(df_accident_original) - len(df_accident))


# ------ 최종 확인 ------
print("전처리 완료 (df_detail):")
print(df_detail.head(20))

print()

print("전처리 완료 (df_accident):")
print(df_accident.head(20)) # 사고가 없는 연도/보증종류도 분석에 의미가 있을 수 있으니, 0값 자체로 데이터를 제거하면 안된다네요

# 2016년부터 2024년까지 기간 필터링 변수
start_year = 2016
end_year = 2025

# 전세 보증보험 가입 건수 (df_detail)
df_detail_filtered = df_detail[
    (df_detail['발급년도'] >= start_year) & (df_detail['발급년도'] <= end_year) &
    (df_detail['상품명'].str.contains("전세보증금반환보증"))
]

detail_yearly = df_detail_filtered.groupby('발급년도')['건수'].sum().reset_index()

#---------- 보증 사고 건수 (df_accident)-------------
df_accident_filtered = df_accident[
    (df_accident['연도'] >= start_year) & (df_accident['연도'] <= end_year)
]
accident_yearly = df_accident_filtered.groupby('연도')['건수'].sum().reset_index()

# 주택유형별 가입 건수 합계 계산
housing_type_counts = df_detail.groupby('주택유형')['건수'].sum().reset_index()
housing_type_counts = housing_type_counts.sort_values(by='건수', ascending=False).head(4)

# 그래프 그리기
plt.figure(figsize=(10,6))
sns.barplot(data=housing_type_counts, x='건수', y='주택유형', palette='pastel')
plt.title('주택유형별 전세보증 가입 건수',fontsize=18, fontweight='bold', pad=15)
plt.xlabel('가입 건수')
plt.ylabel('주택유형')
plt.grid(axis='x')
plt.show()

# ---------------지역별 전세보증 그래프 -----------------

# 지역별 가입 건수 합계 계산 및 내림차순 정렬
region_counts = df_detail.groupby('지역')['건수'].sum().reset_index()
region_counts = region_counts.sort_values(by='건수', ascending=False)

# 그래프 그리기
plt.figure(figsize=(12,8))
sns.barplot(data=region_counts, x='건수', y='지역', palette='Set3')
plt.title('지역별 전세보증 가입 건수',fontsize=18, fontweight='bold', pad=15)
plt.xlabel('가입 건수')
plt.ylabel('지역')
plt.grid(axis='x')
plt.show()

import matplotlib.pyplot as plt

# 지역별 가입 건수 합계 계산 및 내림차순 정렬
region_counts = df_detail.groupby('지역')['건수'].sum().reset_index()
region_counts = region_counts.sort_values(by='건수', ascending=False)

# 상위 10개 지역만 표시 (너무 많으면 복잡해져요)
top_n = 5
top_regions = region_counts.head(top_n)
others = pd.DataFrame({
    '지역': ['기타'],
    '건수': [region_counts['건수'][top_n:].sum()]
})

pie_data = pd.concat([top_regions, others], ignore_index=True)

# 파이차트
plt.figure(figsize=(8, 8))
colors = sns.color_palette('pastel')[0:len(pie_data)]

plt.pie(
    pie_data['건수'],
    labels=pie_data['지역'],
    autopct='%.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'white'}
)

plt.title('지역별 전세보증 가입 건수 비율 (상위 5개 + 기타)', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()


# --------------전세 보증보험 가입 건수 그래프---------------
plt.figure(figsize=(12,6))
sns.lineplot(
    data=detail_yearly, 
    x='발급년도', 
    y='건수', 
    marker='o', 
    color="#5CC596",           # 파란 계열로 변경
    label='전세 보증보험 가입 건수',
    linewidth=2.5,
    markersize=8
)

plt.title('2016-2025년 전세 보증보험 가입 건수 추이', fontsize=18, fontweight='bold', pad=15)
plt.xlabel('연도', fontsize=14)
plt.ylabel('건수', fontsize=14)

plt.xticks(range(start_year, end_year + 1), fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)

# 테두리 제거
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()


# -----------------보증 사고 건수 그래프-------------------
plt.figure(figsize=(12,6))
sns.lineplot(
    data=accident_yearly,
    x='연도',
    y='건수', 
    marker='o',
    color="#FF8F83", 
    label='보증 사고 건수', 
    linewidth=2.5, 
    markersize=8)

plt.title('2016-2023년 보증 사고 건수 추이', fontsize=18, fontweight='bold', pad=15)
plt.xlabel('연도', fontsize=14)
plt.ylabel('건수', fontsize=14)

plt.xticks(range(start_year, end_year + 1), fontsize=12)
plt.yticks(fontsize=12)

plt.legend(fontsize=13)
plt.grid(True, linestyle='--', alpha=0.6)

# 테두리 선 제거해서 깔끔하게
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# ------------- 보증 사고 유형별 그래프 -------------

# 사고 유형별 분석집계
accident_by_type = df_accident.groupby('보증종류')['건수'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(
    data=accident_by_type.sort_values('건수', ascending=False),  # 큰 순서로 정렬
    x='건수', 
    y='보증종류', 
    palette='Set2' 
)

plt.title('보증 사고 유형별 사고 건수', fontsize=18, fontweight='bold', pad=15)
plt.xlabel('사고 건수', fontsize=12)
plt.ylabel('보증 종류', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 격자와 테두리 조정
plt.grid(axis='x', linestyle='--', alpha=0.5)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

# 사고 유형별 건수 집계
accident_by_type = df_accident.groupby('보증종류')['건수'].sum().reset_index()

# 사고 유형별 건수 집계 후 내림차순 정렬
accident_by_type = df_accident.groupby('보증종류')['건수'].sum().reset_index()
accident_by_type = accident_by_type.sort_values(by='건수', ascending=False)

# 상위 5개만 선택
accident_top5 = accident_by_type.head(5)

# 파이차트 그리기
plt.figure(figsize=(8, 8))
colors = sns.color_palette('pastel')[0:5]

plt.pie(
    accident_top5['건수'],
    labels=accident_top5['보증종류'],
    autopct='%.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops={'edgecolor': 'white'}
)

plt.title('보증 사고 유형별 상위 5개 비율', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()
