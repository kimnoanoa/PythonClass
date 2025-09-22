# 함수

def add(a,b):
    return a + b

hap =add(3,4) # 숫자로 넣어서, 변수로 받아서 출력
print(hap)

c = 5
d = 6

hap = add(c,d) # 변수로 넣어서, 변수로 받아서 출력하기
print(hap)

print(add(8,9)) # 숫자 넣어서 , 바로 출력하기

print("---------입력값이 있는 함수----------")

# 조금 더 정석적으로 표현
def add(a,b):           # a, b 는 매개변수(parameter)
    result = a + b
    return result

hap = add(4,7)          # 4, 7 은 인수(arguments)
print(hap)
print()

print("---------입력값이 없는 함수----------")
print()

def say():
    return 'hi'

a = say()
print(a)

def say2():
    print("hi")
    
say2()
a = say2()
print(a)
print(say2())

print("---------입력값만 있는 경우----------")
print()

def add2(a,b):
    print(f'{a}와 {b}의 합은 {a + b} 입니다.')
    
add2(3,4)


print("---------헷갈리게 혼합하기----------")
print()

def add2(a,b):
    print(f'{a}와 {b}의 합은 {a + b} 입니다.')
    print(f'하지만 반환하는 값은 {a} X {b} 입니다.')
    result = a * b
    return result
    
a = add2(3,4)
print(a)

print("----매개변수 지정하여 입력----")

def sub(a,b):
    return a - b

result = sub(3,4)
print(result)

result = sub(b = 5,a = 9) # 매개변수 지정하면 순서가 달라도 된다.
print(result)

# 4가지 경우 만들어보세요.
print("------------------------")

def cal(a,b):
    return a / b

result = cal(7,2)
print(result)

def noa():
    return "noa"

a = noa()
print(a)

def cal2(a,b):
    return a * b

result = cal2(15,20)
print(result)

result = cal2(33,27)
print(result)


def cal3(a,b):
    print(f'{a}와 {b}의 합 : {a+b}')
    print(f'실제 함수 출력 값 : {a * b}')
    result = a * b
    return result

a = cal3(10,12)
print(a)