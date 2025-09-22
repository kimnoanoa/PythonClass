people = 0
count = 0
while people < 10:
    people += 1
    print(f"{people}명 입장했습니다.")

    if people % 5 == 0:
        print("정원 초과 입니다.")
        count += 1
        print(f"{count}회 운행했습니다.")