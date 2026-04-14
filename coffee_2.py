quantity = 10
price = 500

print(f"남은 커피 수량: {quantity}개")

while quantity > 0:
    money = int(input("돈을 넣으세요: "))
    
    if money >= price:
        change = money - price
        quantity = quantity - 1
        print("커피 나왔습니다☕️")
        print(f"거스름돈: {change}원")
        
        if quantity > 0:
            print(f"남은 커피 수량: {quantity}개")
        else:
            print("커피가 모두 판매되었습니다. 자판기를 종료합니다.")
    else:
        print("금액이 부족합니다😭")
        print(f"남은 커피 수량: {quantity}개")
