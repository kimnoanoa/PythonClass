# for문

test_list ={'one','two','three'}

print(test_list)

for i in test_list:
    print(i)
    
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)
    
print()
print("--------for 문 응용 ------------")
print()

marks = [90,25,67,45,80]
number =0

for mark in marks:
    number = number + 1
    if mark >= 60:
        print(f'{number}번 학생 합격입니다.')
    else:
        print(f'{number}번 학생 불합격입니다.')
        
print("--------for 문 continue ------------")

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d 번 학생 축하합니다. 합격입니다!"  %number)
    
print("--------for 문 range ------------")
    
a = range(10)
print(a)

a = range(1,11)
print(a)

add = 0
for i in range(1,11):
    add = add + i

print(add)

for i in range(5):
    print("안녕하세요")
    
marks = [90,25,67,45,80]
for number in range(len(marks)):
    print("시험 수고하셨습니다.")
    
print()
# for 문 구구단 짜보기

print("-----for문 구구단!-----")
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}', end='\t')
    print()
