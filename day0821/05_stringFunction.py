# 문자열 관련 내장함수

a = "hobby"
print(a.count('b'))

print()
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))  # 찾는 값 없을 때는 -1 반환

print()
a = "Python is the best choice"
print(a.index('b'))
# print(a.index('k')) 찾는 값 없을 때는 에러 

print()
a = 'abcd'
print(",".join(a))  #a,b,c,d

print()
b = ['a', 'b', 'c', 'd']
print(".".join(b))  #a.b.c.d

print()
a = "hi"
print(a.upper())

a = "HI"
print(a.lower())

print()
print("-----스트립-----")
print()

a = "  hi  "
print(a)
print(a.lstrip())  # 왼쪽 공백 제거
print(a.rstrip())  # 오른쪽 공백 제거
print(a.strip())   # 양쪽 공백 제거

print()
print("----------")
print()

a = "Life is too short"
b = a.replace("Life", "Movie")
print(b)

print()
a = "Life is too short"
b = a.split()
print(b)

print()
a = "Life:is:too:short"
b = a.split(':')
print(b)

print()
print("---문자열이 알파벳으로만 이루어졌는지 확인---")

s = "Python"
print(s.isalpha()) # 알파벳만 있기 때문에 True

s = "Python3"
print(s.isalpha())  # 숫자가 있어서 False

s = "Hello world"
print(s.isalpha())  # 공백이 있어서 False

print()
print("---문자열이 숫자로만 이루어졌는지 확인---")

s = "12345"
print(s.isdigit())
s = "1234a"
print(s.isdigit())
s = "12 45"
print(s.isdigit())

print()
print("---문자열이 특정 문자(열)로 시작/끝 하는지 확인---")

s = "Life is too short"
print(s.startswith("Life"))
print(s.startswith("too"))
print()
print(s.endswith("short"))
print(s.endswith("is"))

a = 'hi'
print(a.upper())  # HI
print(a)          # hi
a = a.upper()
print(a)          # HI











