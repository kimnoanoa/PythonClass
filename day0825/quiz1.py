students = ['민수','지영','철수','영희']
points = [3,-2,0,5]


# 5점 이상 : '칭찬대상'  0점 초과 5점 미만 : '일반 학생' 0점 이하 : 주의필요

#최종 결과

print()
print()


for name, point in zip(students,points):
    if point >= 5:
        score = "칭찬 대상"
    elif point <= 0:
        score = "주의 필요"
    else:
        score = "일반 학생"
    print(f'{name} : {score}')
    

    