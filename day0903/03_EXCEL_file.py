# 확장프로그램 Excel Viewer 설치
# pip install openpyxl

import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)

df1 = pd.read_excel('data\남북한발전전력량.xlsx')
print(df1)

print()

df2 = pd.read_excel('C:\\Users\\admin\\Desktop\\PythonClass\\data\\남북한발전전력량.xlsx', header=None)
print(df2)
print()