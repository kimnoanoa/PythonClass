print("---정수형---")
a = 123
print(a)
a = -179
print(a)
a = 0
print(a)

print()
print("---소수형---")
a=1.2
print(a)
a = -3.45
print(a)
a = 4.24E10 #E10 = 10의 10제곱 = 10000000000
print(a)
a=4.24e-10 #e-10 = 10의 -10제곱 =0.0000000001
print(a)

print("---8진수와 16진수---")
print("---8진수---")
a = 0o177   #  1x8(2제곱)  +  7x8(1제곱)  +  7x8(0제곱)
            #  64 + 56 + 7 =127
print(a)
print("---16진수---")
# 1 2 3 4 5 6 7 8 9 A B C D E F
a = 0x8ff
b = 0xABC   #  Ax16(2제곱) + Bx16(1제곱) + Cx16(0제곱)
            # 10x256 + 11x16 + 12x1 = 2748
print(b)

