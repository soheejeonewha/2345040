# 구구단 프로그램
# 사용자로부터 원하는 단을 입력
dan = int(input("몇 단을 출력할까요: "))
# 실행 결과
for i in range(1, 10):
    print(f"{dan} * {i} = {dan * i}")