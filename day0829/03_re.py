import re


p = re.compile('a.b')
m = p.match('a\nb') #라인개행만큼은 못찾음.
print(m)

p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb') #  라인개행까지 포함해서 매치
print(m)

print("----- IGNORECASE -----")
print()

p = re.compile('[a-z]+',re.I)
m = p.match('python')
print(m)
m = p.match('Python')
print(m)
m = p.match('PYTHON')
print(m)
m = p.match('python')
print(m)

print("----- MULTILINE -----")
print()

p = re.compile("^python\s\w+")

data = """
python one
life is too short
python two
you need python
python three
"""
m = p.findall(data)
print(m)
