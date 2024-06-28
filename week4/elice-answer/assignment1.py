def buy(num):
    global total
    if num > total:
        print("구매가능 수량을 초과했습니다.")
    else:
        total -= num
        print(f"{num}개 구매하였습니다.")
    print(f"남은 수량: {total}개")


# 아래 실행영역은 수정하지 않습니다.
total = 100
apples = int(input("구매할 수량: "))
buy(apples)
