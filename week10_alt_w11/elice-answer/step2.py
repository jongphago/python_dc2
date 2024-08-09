burgers = ["불고기버거", "새우버거", "치즈버거"]
drinks = ["스프라이트", "우유", "콜라"]
orderList = []


# Deprecated: orderBurger 함수를 order 함수로 대체
def orderBurger(menu):
    if menu in burgers:
        orderList.append(menu)
        print(f"{menu} 추가 완료")
    else:
        print("없는 메뉴입니다.")

# Deprecated: orderDrink 함수를 order 함수로 대체
def orderDrink(menu):
    if menu in drinks:
        orderList.append(menu)
        print(f"{menu} 추가 완료")
    else:
        print("없는 메뉴입니다.")
        
# orderBurger 함수와 orderDrink 함수를 order 함수로 대체
def order(type, menu):
    if menu in type:
        orderList.append(menu)
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
        # orderBurger 함수를 order 함수로 대체
        # orderBurger(myBurger)
        order(burgers, myBurger)
    elif orderType == 2:
        myDrink = input("추가할 음료:")
        # orderDrink 함수를 order 함수로 대체
        # orderDrink(myDrink)
        order(drinks, myDrink)
    elif orderType == 3:
        print("주문을 종료합니다.")
        break
    # orderType이 1, 2, 3이 아닌 경우
    else:
        print("다시 입력해 주세요.")
