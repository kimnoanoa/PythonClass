import re

p = re.compile('ab*')

# p = 패턴객체
# 패턴객체 메서드의 종류

# match() - 문자열의 처음부터 정규식과 매치되는지 조사
# search() - 문자열 전체를 검색하여 정규식과 매치되는지 조사
# findall() - 정규식과 매치되는 모든 문자열을 리스트로 반환
# finditer() - 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 반환

# match, search 는 정규식과 매치될 때는 match 객체를 반환하고
# 매치되지 않을 때는 None 을 반환

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

result = p.findall("life is too short")
print(result)

result = p.finditer("life is too short")
print(result)

for r in result:
    print(r)
    
# match 객체의 메서드 종류
# group -  매치된 문자열을 반환
# start - 매치된 문자열의 시작 위치를 반환
# end - 매치된 문자열의 끝 위치를 반환
# span - 매치된 문자열의 (시작,끝) 에 해당되는 튜플을 반환

m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

text = '나는 사과와 바나나를 좋아해'

p = re.compile('바나나')
m = p.search(text)
print(m)
print(m.group)
print(m.span())

lst = p.findall(text)
print(lst)
# print(lst.group()) --> findall 은 안됩니다.

find_it = p.finditer(text)
print(find_it)
for match in find_it:
    print(match.group(), match.start())


print()
print("----- 축약형 -----")

p = re.compile('[a-z]+')
m = p.match("python")

# 아래처럼 축약 가능

m = re.match('[a-z]+' , 'python')

