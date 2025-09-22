# bool 자료형
# True: 참
# False: 거짓

a = True
b = False

print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

print(1 == 1) # True
print(2 > 1) # True
print(2 < 1) # False

# 자료형에도 참과 거짓이 있다!?
# "hello" 참     "" 거짓
# [1,2,3] 참     [] 거짓
# (1,2,3) 참     () 거짓
# {'a':1} 참     {} 거짓
# 1       참     0  거짓   --- 0 이외의 숫자 = 참
# None 거짓

a = [1, 2, 3, 4]
while a:
    print(a.pop())

# while 조건문:
#      수행할_문장   
print()
print("----------")
if [1, 2, 3]: 
    print("참")
else:
    print("거짓")

print()
print("----------")
if []:
    print("참")
else:
    print("거짓")

print()
print("----------")
print(bool('python')) # True
print(bool('')) # False

a = [1, 2, 3]
b = []
c = (1, 2)
d = ()

print(bool(a)) # 리스트 참
print(bool(b)) # 리스트 거짓
print(bool(c)) # 튜플 참
print(bool(d)) # 튜플 거짓
print(bool(-1)) # 숫자 참
print(bool(0)) # 숫자 거짓

print()
print("-----논리 연산자-----")

print() # 둘다 참이어야 참 (= 하나라도 거짓이면 거짓)
print("-----and-----")  
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

print() # 하나만 참이어도 참
print("-----or-----") 
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print() # 반대
print("-----not-----")
print(not True) # False
print(not False) # True
print(not 1) # False
print(not 0) # True

print() 
print("-----예제-----")
x = 5
y = 10
print(x > 0 and y > 0)  # True
print(x > 10 or y > 5)  # True
print(x > 10 or y <= 10)  # True
print(not (x > y))  # True



