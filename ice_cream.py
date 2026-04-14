# 아이스크림 할인 판매
# 아이스크림 한 개의 가격
price = 1500

# 3개 이상 구매 시 할인가
discount_price = 1000

# 아이스크림 개수 입력
quantity = int(input("아이스크림 개수: "))

# 3개 이상 구매 여부
total = 0
while quantity >= 3:
    total = quantity * discount_price
    break
while quantity < 3:
    total = quantity * price
    break

# 총 금액 출력
print(f"총 금액: {total}원")