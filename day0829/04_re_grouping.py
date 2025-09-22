# !!!! 그루핑 !!!!
# 1. 여러 문자를 하나로 묶어서 반복 처리
# 매치된 문자열에서 원하는 부분만 추출

import re

p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m) # <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group()) #ABCABCABC

# 이름 부분만 추출하고 싶다면?
p = re.compile(r"(\w+)\s+((\d)+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m)
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring').group()
print(m)
print()

print("----- 이메일 사용자명과 도메인 분리 -----")
text = '문의 : hello.world@python.org'
pattern =r"(([a-zA-z0-9._%+-])+@([a-zA-z0-9.-]+\.[a-zA-z]{2,}))"

match = re.search(pattern)
print("전체:",match.group(1))
print("사용자명:",match.group(2))
print("도메인:",match.group(3))