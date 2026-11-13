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


# 정해진 범위(low~high)의 정수를 올바르게 입력받을 때까지 반복해서 묻는 함수
# prompt: 화면에 보여줄 문구 / low, high: 허용하는 최솟값, 최댓값  (매개변수)
def read_int(prompt, low, high):
    while True:                                  # 올바른 값이 나올 때까지 계속 묻는다
        text = input(prompt).strip()             # 입력받고 앞뒤 공백을 지운다 (" 1 " → "1")

        if text == "":                           # 아무것도 안 쓰고 Enter만 친 경우
            print("⚠️ 아무것도 입력하지 않았습니다. 숫자를 입력하세요.")
            continue                             # 반복문 맨 위로 돌아가 다시 입력받는다

        try:
            number = int(text)                   # 글자를 정수로 바꿔본다
        except ValueError:                       # abc처럼 바꿀 수 없으면 에러가 나는데, 여기서 붙잡는다
            print(f"⚠️ 숫자가 아닙니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue

        if number < low or number > high:        # 숫자이긴 한데 범위 밖인 경우 (9, 0 등)
            print(f"⚠️ 범위를 벗어났습니다. {low}-{high} 사이의 숫자를 입력하세요.")
            continue

        return number                            # 모든 검사를 통과하면 값을 돌려주고 함수를 끝낸다


# 프로그램 전체 흐름을 담당하는 함수
def main():
    try:                                         # Ctrl+C나 입력 끊김이 생겨도 이 안에서 처리한다
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)    # 이제 choice는 글자가 아니라 숫자(int)다

            if choice == 1:                      # 숫자이므로 따옴표 없이 비교한다
                print("퀴즈 풀기는 아직 준비 중입니다.")
            elif choice == 2:
                print("퀴즈 추가는 아직 준비 중입니다.")
            elif choice == 3:
                print("퀴즈 목록은 아직 준비 중입니다.")
            elif choice == 4:
                print("점수 확인은 아직 준비 중입니다.")
            elif choice == 5:
                print("게임을 종료합니다. 안녕히 가세요!")
                break
    except (KeyboardInterrupt, EOFError):        # Ctrl+C(KeyboardInterrupt) 또는 입력 끊김(EOFError)
        print("\n\n입력이 중단되어 안전하게 종료합니다.")


# 이 파일을 직접 실행했을 때만 main()을 호출한다
if __name__ == "__main__":
    main()


# 이 파일을 직접 실행했을 때만 main()을 호출한다
if __name__ == "__main__":
    main()
