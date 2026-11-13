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

# 퀴즈 한 문제를 표현하는 클래스 (설계도)
class Quiz:
    # 객체가 만들어질 때 자동 실행된다. self는 만들어지는 객체 자신이다
    def __init__(self, question, choices, answer):
        self.question = question    # 속성: 문제 글
        self.choices = choices      # 속성: 선택지 4개가 담긴 리스트
        self.answer = answer        # 속성: 정답 번호 (1~4, 숫자)

    # 문제와 선택지를 화면에 보여주는 메서드
    def display(self):
        print(self.question)
        # enumerate: 리스트를 돌면서 번호를 같이 준다. start=1이라 1번부터 시작한다
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    # 사용자가 고른 번호가 정답인지 확인하는 메서드. True/False를 돌려준다
    def is_correct(self, user_answer):
        return user_answer == self.answer


# 기본 퀴즈 데이터(영화 주제)를 만들어 리스트로 돌려주는 함수
def create_default_quizzes():
    # Quiz(문제, [선택지 4개], 정답 번호) 형태로 퀴즈 객체를 만들어 리스트에 담는다
    quizzes = [
        Quiz(
            "영화 '타이타닉'(1997)을 연출한 감독은?",
            ["크리스토퍼 놀란", "스티븐 스필버그", "제임스 카메론", "조지 루카스"],
            3,    # 정답: 3번 제임스 카메론
        ),
        Quiz(
            "영화 '해리 포터' 시리즈에서 해리가 다니는 마법 학교의 이름은?",
            ["호그와트", "보바통", "덤스트랭", "일버모니"],
            1,    # 정답: 1번 호그와트
        ),
        Quiz(
            "애니메이션 '겨울왕국'에서 엘사가 부르는 대표곡은?",
            ["하쿠나 마타타", "렛 잇 고", "어 홀 뉴 월드", "컬러스 오브 더 윈드"],
            2,    # 정답: 2번 렛 잇 고
        ),
        Quiz(
            "영화 '살인의 추억', '괴물', '기생충'을 연출한 감독은?",
            ["박찬욱", "김지운", "류승완", "봉준호"],
            4,    # 정답: 4번 봉준호
        ),
        Quiz(
            "영화 '반지의 제왕'에서 절대반지를 운반하는 '반지의 사자' 역할을 맡은 호빗은?",
            ["빌보", "프로도", "샘", "피핀"],
            2,    # 정답: 2번 프로도
        ),
    ]
    return quizzes    # 만든 퀴즈 리스트를 호출한 곳으로 돌려준다


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


# 퀴즈를 순서대로 출제하고 결과(점수)를 돌려주는 함수
# quizzes: Quiz 객체가 담긴 리스트 (매개변수)
def play_quiz(quizzes):
    if len(quizzes) == 0:                        # 퀴즈가 하나도 없으면
        print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
        return None                              # 점수 없음. 값 없이 함수를 끝낸다

    print(f"\n📝 퀴즈를 시작합니다! (총 {len(quizzes)}문제)")
    correct_count = 0                            # 맞힌 개수를 세는 변수. 0에서 시작한다

    # for: 정해진 횟수(퀴즈 개수)만큼 반복한다. enumerate로 문제 번호도 같이 받는다
    for index, quiz in enumerate(quizzes, start=1):
        print("-" * 40)
        print(f"[문제 {index}]")
        quiz.display()                           # Quiz 객체의 메서드로 문제를 출력한다
        user_answer = read_int("정답 입력: ", 1, 4)   # 1~4만 받는다. 잘못 쓰면 다시 묻는다

        if quiz.is_correct(user_answer):         # Quiz 객체의 메서드로 정답 확인
            print("✅ 정답입니다!")
            correct_count += 1                   # 맞혔으면 1 증가
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

    total = len(quizzes)
    score = correct_count * 100 // total         # 100점 만점 점수. //는 소수점 버리는 나눗셈이다
    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
    print("=" * 40)
    return score                                 # 점수를 돌려준다 (S7에서 최고 점수 비교에 쓴다)



# 프로그램 전체 흐름을 담당하는 함수
def main():
    quizzes = create_default_quizzes()   # 기본 퀴즈 리스트를 만들어 변수에 담아 둔다

    try:                                         # Ctrl+C나 입력 끊김이 생겨도 이 안에서 처리한다
        while True:
            show_menu()
            choice = read_int("선택: ", 1, 5)    # 이제 choice는 글자가 아니라 숫자(int)다

            if choice == 1:                      # 숫자이므로 따옴표 없이 비교한다
                play_quiz(quizzes)
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