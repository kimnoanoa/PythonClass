import pandas as pd

# Timestamp의 배열 만들기 - 월 간격 (시작일 기준)
ts_ms = pd.date_range(start='2024-01-01',
                      end=None,
                      periods=6,
                      freq='MS',
                      tz='Asia/Seoul')
print(ts_ms)
print()
print(type(ts_ms))
print(type(ts_ms[0]))
print()

# 월말 기준
ts_me = pd.date_range(start='2024-01-01',
                      end=None,
                      periods=6,
                      freq='ME',
                      tz='Asia/Seoul')
print(ts_me)
print()

# 3개월 간격, 월초
ts_3m = pd.date_range(start='2024-01-01',
                      end=None,
                      periods=6,
                      freq='3MS',
                      tz='Asia/Seoul')
print(ts_3m)
print()

'''
D - 1일
B - 영업일
W - 주간
H - 시간
T / min - 분
S - 초

M - 월
MS - 월초
Q - 분기 (3/6/9/12)
QS - 분기 시작 달 첫날
Y - 년
YS - 년초

2D - 2일 간격
3H - 3시간
'''