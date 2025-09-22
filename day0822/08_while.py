# while 문

sleep = 0 

i = 0
while sleep < 10:
    sleep = sleep + 1
    i = i + 1
    print(f"잠을 {sleep}시간째 자고 있습니다.")
    print(f"도둑이 {i}회 들었습니다.")
    if sleep == 10:
        print("잡았다 요놈!!!")

print()
print()

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())



