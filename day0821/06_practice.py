info = '970301-1234567홍길동M'
by = info[:2]
bm = info[2:4]
bd = info[4:6]
name = info[-4:-1]
gen = info[-1]

print(f'이름\t년도\t월\t일\t성별\t\n{name}\t{by}\t{bm}\t{bd}\t{gen}')