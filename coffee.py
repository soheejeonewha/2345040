# 커피 자판기
# 커피 한 잔 가격
price = 500

# 넣은 돈
money = int(input("돈을 넣으세요: "))

# 500원 이상인지 확인
while money >= price:
    print("커피 나왔습니다.")
    # 거스름돈 계산
    change = money - price
    print(f"거스름돈: {change}원")
    break
while money < price:
    print("금액이 부족합니다.")
    break