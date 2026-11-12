# 메뉴 화면을 출력하는 함수. 값을 돌려주지 않고 화면에 보여주기만 한다
def show_menu():
    print("=" * 40)                 # "=" 문자를 40번 반복해서 구분선을 만든다
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)


# 프로그램 전체 흐름을 담당하는 함수
def main():
    while True:                     # 종료를 고를 때까지 메뉴를 계속 반복한다
        show_menu()                 # 위에서 만든 함수를 호출해 메뉴를 보여준다
        choice = input("선택: ").strip()   # 입력받고 앞뒤 공백을 지운다. choice는 입력값을 담는 변수다

        if choice == "1":           # 입력이 "1"이면
            print("퀴즈 풀기는 아직 준비 중입니다.")
        elif choice == "2":         # 아니고 "2"이면
            print("퀴즈 추가는 아직 준비 중입니다.")
        elif choice == "3":
            print("퀴즈 목록은 아직 준비 중입니다.")
        elif choice == "4":
            print("점수 확인은 아직 준비 중입니다.")
        elif choice == "5":
            print("게임을 종료합니다. 안녕히 가세요!")
            break                   # 반복문을 빠져나가 프로그램을 끝낸다
        else:                       # 위 어디에도 해당하지 않으면 (abc, 9, 빈 입력 등)
            print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")


# 이 파일을 직접 실행했을 때만 main()을 호출한다
if __name__ == "__main__":
    main()
