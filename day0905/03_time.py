import pandas as pd

# Period 배열 만들기

pr_m = pd.period_range(start='2024-01-01',
                       end=None,
                       periods=3,
                       freq='M')
print(pr_m)
print()

# 1시간 간격
pr_h = pd.period_range(start='2024-01-01',
                       end=None,
                       periods=3,
                       freq='H')
print(pr_h)
print()

# 2일 주기
pr_2d = pd.period_range(start='2024-01-01',
                       end=None,
                       periods=3,
                       freq='2d')
print(pr_2d)
print()