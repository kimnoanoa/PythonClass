# 정규 표현식
# 암호 해독학 (by 제이엠)
import re

data =[
    {'name': 'park','resNum':'800905-1257289'},
    {'name': 'kim','resNum':'991122-2222222'},
    {'name': 'Lee','resNum':'000504-1445454'}
]

for person in data:
    name = person['name']
    front, _ = person['resNum'].split('-') 
    masked = front + '-*******'             
    print({'name': name, 'resNum': masked})
    
data2 ="""
park 800905-1010101
kim  700905-1010121
"""

pat = re.compile("(\d{6})-\d{7}")
print(pat.sub("\g<1>-*******",data2))



    

print('123'.isdigit())
print('a123'.isdigit())

words = ['apple','banana','mango']

print(" ".join(words)) 

# 주민번호 뒷자리 별표처리

# park 800905 - *******
# kim  700905 - *******




    




