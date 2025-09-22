import re

s = '<html><head><title>Title</title>'

print(len(s))

print(re.match('<.*>', s).span())

print(re.match('<.*>', s).group())

print(re.match('<.*?>', s).group())

# *? +? {m,n}?

text = '1234567 홍길동 1 #$123홍길동'
pattern = r'\d{2,4}?'

matches = re.findall(pattern, text)
print(matches)
print()

print("----- 괄호 안의 내용 뽑기 -----")
print()

text = '오늘 메뉴는 (자장면) 과 (오징어덮밥) 입니다.'

pattern = r"\((.*?)\)"

menus = re.findall(pattern, text)
print(menus)

# ['(자장면)', '(오징어덮밥)']


