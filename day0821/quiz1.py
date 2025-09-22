info = '970301-1234567홍길동M'

# 프린트문은 한개만 써서!

name = info[14:17]
year = info[0:2]
mont = info[2:4]
day = info[4:6]
gender = info[-1]
print("이름\t년도\t월\t일\t성별")
print(name + "\t" + year + "\t" + mont + "\t" + day + "\t" + gender)
print(f"{info[14:17]}\t{info[0:2]}\t{info[2:4]}\t{info[4:6]}\t{info[-1]}")