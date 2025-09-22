# 딕셔너리 관련 함수
a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print()
print("-----키값 뽑아오기-----")
print(a.keys())  # dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)

b = list(a.keys()) # 리스트로 변환
print(b)

print()
print("-----밸류값 뽑아오기-----")

print(a.values()) # dict_values(['pey', '010-9999-1234', '1118'])
c = list(a.values())
print(c) # ['pey', '010-9999-1234', '1118']

print()
print("-----키,밸류 뽑아오기-----")
print(a.items())
d = list(a.items())
print(d)

print()
print("-----키,밸류 지우기-----")
print(a)
a.clear()
print(a)

print()
print("-----get-----")
a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
print(a['name'])
print(a.get('name'))
print(a.get('phone'))

# print(a['hobby']) --- 해당 키값 없으면 오류 --- KeyError: 'hobby'
print(a.get('hobby'))  # 키값 없으면 None 반환
print(a.get('hobby', '정보없음'))

print()
print("-----in-----")
print('name' in a)
print('hobby' in a)

print()
print("-----pop-----")
name = a.pop('name')
print(name)
print(a)

email = a.pop('email', '정보없음')
print(email)

