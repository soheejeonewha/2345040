# 엘리베이터 프로그램
# 사용자로부터 시작층 입력
floor = int(input("시작층을 입력하세요: "))

# 시작층부터 1층까지 이동
while floor >= 1:
    print(f"▼ {floor}층")
    floor = floor - 1
print("1층 도착!")
# while 루프가 1층에 도착하면 반복이 종료되는 조건이 보다 명확하게 드러난다고 판단했습니다!