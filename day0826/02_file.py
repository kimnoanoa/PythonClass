# 파일 읽고 쓰기

# r - 읽기 모드 : 파일을 읽기만 할 때 사용한다.
# w - 쓰기 모드 : 파일에 내용을 쓸 때 사용한다.
# a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

f = open("./day0826/새파일.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = f'{i}번째 줄입니다.\n'
    f.write(data) # 메모장에 쓸 때는 문자열을 넣어야 한다.
f.close()
print()


print("-----읽기 모드 (readline)-----")
print()

f = open("./day0826/새파일.txt", 'r', encoding="utf-8")
line = f.readline() # 첫 번째 줄을 반환
print(line)
f.close()
print()

print("-----while 문으로 여러줄 읽기-----")
print()

f = open("./day0826/새파일.txt", 'r', encoding="utf-8")
while True:
    line = f.readline() # 첫 번째 줄을 반환
    if not line: break
    print(line)
f.close()
print()

print("-----readlines 로 읽기-----")
print()

f = open("./day0826/새파일.txt", 'r', encoding="utf-8")
lines = f.readlines() # 파일의 각각의 줄을 요소로 하는 리스트 반환
print(lines)

for line in lines:
    line = line.strip()
    print(line)

f.close()
print()

print("-----read 로 읽기-----")
print()

f = open('./day0826/새파일.txt', 'r', encoding='utf-8')
data = f.read() # 파일 내용 전체를 문자열로 반환
print(data)
f.close()
print()

print("-----객체로 읽기-----")
print()

f = open('./day0826/새파일.txt', 'r', encoding='utf-8')
for line in f:
    print(line)
f.close()
print()

print("-----추가하기 모드-----")
print()

f = open('./day0826/새파일.txt', 'a', encoding='utf-8')
for i in range(11, 21):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()
print()

print("-----with문과 함께 사용하기-----")
print()

# f = open("./day0826/poo.txt", 'w', encoding='utf-8')
# f.write("Life is too short, you need python")
# f.close()

# # 위 내용이랑 똑같이 작동
# with open("./day0826/poo.txt", 'w', encoding='utf-8') as f:
#     f.write("Life is too short, you need python")

print()
print("-----os.path.exists-----")
print()

import os

file_path = './day0826/poo.txt'

if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("Life is too short, you need python")

# 그 다음 작업을 지시 (추가, 읽기 등)

# 함수 안의 변수는 밖의 변수와 상관 없음.
# 블록 안의 변수 (if, for, while, with)는 밖의 변수 그대로임.

