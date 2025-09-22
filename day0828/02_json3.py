import json
import os

filename = "people2.json"

# 파일이 없으면 빈 리스트 저장
if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([], f)

# JSON 파일 불러오기
with open(filename, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

# 이름과 나이 입력 받아서 loaded_data에 추가
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))  # 숫자로 변환

loaded_data.append({"name": name, "age": age})

# JSON 파일로 다시 저장
with open(filename, "w", encoding="utf-8") as f:
    json.dump(loaded_data, f, ensure_ascii=False, indent=4)

# 출력
print()
print(loaded_data)
print()

for person in loaded_data:
    print(f"{person['name']} is {person['age']} years old")
