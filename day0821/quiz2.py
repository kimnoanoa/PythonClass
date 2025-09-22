# 상품 이름
name = ['새우깡', '바나나킥', '양파링', '고래밥', '포카칩']

# 상품 가격
prices = [1200, 1500, 1000, 1800, 2000]

# 판매 개수
quantities = [3, 2, 5, 1, 4]

# 총 매출액을 계산하시오.

a = prices[0]*quantities[0]
b = prices[1]*quantities[1]
c = prices[2]*quantities[2]
d = prices[3]*quantities[3]
e = prices[4]*quantities[4]

sum = a + b + c + d + e


display = f"""
상품명\t\t가격\t판매수량\t매출금액
================================================
{name[0]}\t\t{prices[0]}\t   {quantities[0]}\t\t{a}
{name[1]}\t{prices[1]}\t   {quantities[1]}\t\t{b}
{name[2]}\t\t{prices[2]}\t   {quantities[2]}\t\t{c}
{name[3]}\t\t{prices[3]}\t   {quantities[3]}\t\t{d}
{name[4]}\t\t{prices[4]}\t   {quantities[4]}\t\t{e}
================================================
총 매출 금액 = {sum} 원
================================================
"""
print(display)

