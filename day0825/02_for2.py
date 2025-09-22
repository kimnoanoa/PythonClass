# 리스트 컴프리헨션
# list comprehension

a =[1,2,3,4]
result = []
for num in a:
    result.append(num*3)
    
print(result)

print("-----리스트 컴프리헨션-----")
print()

a =[1,2,3,4]
result =[num * 3 for num in a]
print(result)
print()

result = [num * 3 for num in a if num % 2 == 0]
print(result)
print()

# [결과 for 항목 in 리스트(튜플) if 문]
# for 문을 2개 이상 사용하는 것도 가능하다.

result = [x * y for x in range(2,10)
                for y in range(1,10)]
print(result)

print()

print("-----break-----")
print()

for i in range(10):
    print(i,end=" ")
    if i==5:
        break
print()

print("안녕히 주무세요")

print("---for -else문---")
for i in range(5):
    print(i)
else:
    print("for문 정상종료.")
print()

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for문 정상종료??")
    
print()

print("-----enumerate함수-----")
print()

fruits = ['apple','banana','orange']
for i, fruit in enumerate(fruits):
    print(f'{i} : {fruit}')


for i, fruit in enumerate(fruits,1): # 1부터 시작
    print(f'{i} : {fruit}')
    
print()
print("-----zip 함수-----")
print()

names = ['홍길동', '김철수' ,'이영희']
scores = [85,93,56]

# print(zip(names,scores))

# [('홍길동',85) ('김철수',93)...]
for name, score in zip(names,scores):
    print(f'{name} : {score}점')
    
print()
    
names = ['홍길동', '김철수' ,'이영희','박영수']
scores = [85,93,56]
for name, score in zip(names,scores): # 개수 안맞으면 무시
    print(f'{name} : {score}점')
    
print()

from itertools import zip_longest

for name, score in zip_longest(names,scores ,fillvalue="점수 없음"):
    print(f'{name} : {score}')


print()

names = ['홍길동', '김철수' ,'이영희']
korean = [85,93,56]
english =[90,100,95]
for name, korean,english in zip(names,korean,english):
    print(f'{name} : 국어 {korean}점 , 영어 {english}점')