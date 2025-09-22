
import os

FILENAME = "hotel.txt"

rooms = {
    f"{floor}{room:02d}": "---"
    for floor in range(1, 4)
    for room in range(1, 4)
}
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            for room_no in rooms.keys():
                pass  

def load_rooms():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        room_no, guest = line.split(",")
                        if room_no in rooms:
                            rooms[room_no] = guest
                    except ValueError:
                        pass  

def save_rooms():
    with open(FILENAME, "w", encoding="utf-8") as f:
        for room_no, guest in rooms.items():
            if guest != "---":
                f.write(f"{room_no},{guest}\n")

def show_rooms():
    print()
    for floor in range(3, 0, -1):  
        room_line = []
        guest_line = []
        for room in range(1, 4):
            room_no = f"{floor}{room:02d}"
            room_line.append(room_no.ljust(8))
            guest_line.append(rooms[room_no].ljust(8))
        print("".join(room_line))
        print("".join(guest_line))
    print()

# 체크인 시키기
def check_in():
    room_no = input("입실할 방 번호를 입력하세요 : ").strip()
    if room_no not in rooms:
        print("존재하지 않는 방 번호입니다.\n")
        return
    if rooms[room_no] != "---":
        print("이미 손님이 입실한 방입니다.\n")
        return
    name = input("고객님의 이름을 입력하세요: ").strip()
    if not name:
        print("이름은 비워둘 수 없습니다.\n")
        return
    rooms[room_no] = name
    save_rooms()
    print(f"{room_no}호에 {name}님이 입실하셨습니다.\n")

# 체크아웃시키기
def check_out():
    room_no = input("퇴실할 방 번호를 입력하세요 : ").strip()
    if room_no not in rooms:
        print("존재하지 않는 방 번호입니다.\n")
        return
    if rooms[room_no] == "---":
        print("현재 비어있는 방입니다.\n")
        return
    guest = rooms[room_no]
    rooms[room_no] = "---"
    save_rooms()
    print(f"{room_no}호의 {guest}님이 퇴실하셨습니다.\n")


def main():
    init_file() 
    load_rooms()
    while True:
        print("**********************")
        print("*                    *")
        print("*     NOAH HOTEL     *")
        print("*                    *")
        print("**********************")
        print("[1] 조회 | [2] 입실 | [3] 퇴실 | [4] 종료")
        try:
            choice = int(input("메뉴를 선택하세요: "))
        except ValueError:
            print("숫자만 입력해주세요.\n")
            continue

        if choice == 1:
            show_rooms()
        elif choice == 2:
            check_in()
        elif choice == 3:
            check_out()
        elif choice == 4:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 숫자입니다! 다시 선택하세요.\n")

if __name__ == "__main__":
    init_file()
    main()