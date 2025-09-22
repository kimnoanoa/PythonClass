# 더하기 빼기 곱하기 나누기 제곱 를 입력 받기
# 숫자 두개 를 입력 받기
# 함수 하나에 '연산종류' '숫자두개' 넣어서
# 결과 이쁘게 출력하기
# (0으로 나눌수 없습니다. 이경우는 따로 케어해주세요)

def cal(choice, num1, num2):
    if choice == '1':
        result = num1 + num2
    elif choice == '2':
        result = num1 - num2
    elif choice == '3':
        result = num1 * num2
    elif choice == '4':
        result = round((num1 / num2), 2)
    elif choice == '5':
        result = num1 ** num2

    return result

print("연산 번호를 입력하세요")

while True:

    choice = input("[1]더하기 [2]빼기 [3]곱하기 [4]나누기 [5]제곱 [0]종료 >>> ")

    if choice == '0':
        break

    if choice not in '12345':
        print("입력이 올바르지 않습니다.")
        print()
        continue

    number1 = int(input("첫 번째 숫자 입력: "))
    number2 = int(input("두 번째 숫자 입력: "))

    if choice == '4' and number2 == 0:
        print('0으로 나눌 수 없습니다.')
        print()
        continue

    result = cal(choice, number1, number2)
    print()
    print(f'계산 결과는 {result}입니다.')
    print()


