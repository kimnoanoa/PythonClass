# json 입출력

import json

data = {
    "name" : "Alice",
    "age" : 30,
    "hobbies" : ['reading','traveling'],
    "married" : False,
    "children" : None
}

# 제이슨파일로 덤프하기
with open("basic.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False, indent=4)

# 제이슨파일 로드하기

with open("basic.json","r",encoding="utf-8") as f:
    loaded_data = json.load(f)

print()
print(loaded_data)
print()



    