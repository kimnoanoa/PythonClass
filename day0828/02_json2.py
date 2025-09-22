# 리스트를 제이슨으로 저장 / 로드하기

import json

people = [
    {"name": "Tom","age":25},
    {"name": "Jane","age":28},
    {"name": "Bob","age":22}
]

# 제이슨으로 덤프하기
with open("people.json","w",encoding="utf-8") as f:
    json.dump(people,f,ensure_ascii=False, indent=4)

# 제이슨 파일 불러오기
with open("people.json","r",encoding="utf-8") as f:
    loaded_data = json.load(f)
    

print()
print(loaded_data)
print()

for person in loaded_data:
    print(f'{person['name']} is {person['age']} years old')



# Tom is 25 years old
# Jane is 28 years old
# Bob is 22 years old