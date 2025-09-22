# 람다식

# 함수를 간단하게 만들기

def add(a,b):
    return a + b

add2 = lambda a,b: a+b
result =add2 (3,4)

print(result)

distance = lambda x1,y1,x2,y2: ((x2-x1)**2+(y2 - y1)**2)**0.5
result = distance(1,2,4,6)
print(result)
print()

print("----리스트+맵----")
print()

print("=========================")

numbers = [1,2,3,4,5]
squares = list(map(lambda x: x**2,numbers))

print(squares)
print()

# 리스트 컴프리헨션 방식으로 똑같은 결과 구현하기

numbers =[1,2,3,4,5]
squares = [x ** 2 for x in numbers]
print(squares)

print("=========================")

numbers2 =[1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda x: x % 2 ==0,numbers2))
print(evens)
print()

# 리스트 컴프리헨션 방식으로 똑같은 결과 구현하기

numbers =[1,2,3,4,5,6,7,8,9]
squares = [x for x in numbers2 if x % 2 == 0]
print(squares)

print("=========================")

numbers3 =[5,-2,0,8,-7]

result = list(map(lambda x: "양수" if x > 0 else ("음수" if x < 0 else "0"),numbers3))
print(result)

# 리스트 컴프리헨션 방식으로 똑같은 결과 구현하기

numbers3 = [5, -2, 0, 8, -7]
result = ["양수" if x > 0 else ("음수" if x < 0 else "0") for x in numbers3]
print(result)

print("=========================")


 