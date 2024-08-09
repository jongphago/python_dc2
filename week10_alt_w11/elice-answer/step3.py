burgers = ["불고기버거", "새우버거", "치즈버거"]
drinks = ["스프라이트", "우유", "콜라"]
# orderList를 딕셔너리로 변경
orderList = {}  # orderList = []


def order(type, menu):
    if menu in type:
        # 수량을 입력받아 orderList에 추가
        num = int(input("수량:"))
        # orderList에 메뉴가 이미 있는 경우 수량을 더함
        if menu in orderList.keys():
            orderList[menu] += num
        # orderList에 메뉴가 없는 경우 수량을 추가
        else:
            orderList[menu] = num
        print(f"{menu} 추가 완료")
    else:
        print("없는 메뉴입니다.")

    print("현재 장바구니:", orderList)


# 실행 영역
print("D.Burger 셀프 주문 시스템입니다.")
while True:
    orderType = int(input("메뉴 타입을 번호로 입력하세요 (버거:1/음료:2/종료:3): "))
    if orderType == 1:
        myBurger = input("추가할 버거:")
        order(burgers, myBurger)
    elif orderType == 2:
        myDrink = input("추가할 음료:")
        order(drinks, myDrink)
    elif orderType == 3:
        print("주문을 종료합니다.")
        break
    else:
        print("다시 입력해 주세요.")
