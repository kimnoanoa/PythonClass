# try:
#     a = [1,2]
#     print(a[5])
    
#     b = 4 / 0

# except (ZeroDivisionError,IndexError) as e:
#     print(e)

# try:
#     age = int(input("나이를 입력하세요 : "))
# except:
#     print("입력이 정확하지 않습니다.")
# else:
#     if age <= 18:
#         print("미성년자는 출입금지입니다.")
#     else:
#         print("환영합니다.")
# finally:
#     print("어쨌든 반갑습니당")

students =['김철수','이영희','박민수','최유진']

for student in students:
    try:
        with open(f'{student}_성적.txt') as f:
            score = f.read()
            print(f'{student}의 성적 : {score}')
            
    except FileNotFoundError:
        print(f'{student} 의 성적 파일이 없습니다.')
        continue

print("--------pass---------")
print()

try:
    f = open("설정파일.txt",'r')
    config = f.read()
    f.close()
except FileNotFoundError:
    pass 

print("프로그램이 정상적으로 종료되었습니다.")

        