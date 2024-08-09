# 원하는 버거와 음료를 주문하는 프로그램을 작성해보세요.
# 버거는 불고기버거, 새우버거, 치즈버거가 있고 
# 음료는 스프라이트, 우유, 콜라가 있습니다.
burgers = ["불고기버거", "새우버거", "치즈버거"]
drinks = ["스프라이트", "우유", "콜라"]
orderList = []


# 함수 정의 영역
def orderBurger(menu):
    # 매개변수 menu가 burgers에 있는지 확인
    if menu in burgers:
        # orderList에 menu 추가
        orderList.append(menu)
        print(f"{menu} 추가 완료")
    else:
        print("없는 메뉴입니다.")


def orderDrink(menu):
    # 매개변수 menu가 drinks에 있는지 확인
    if menu in drinks:
        # orderList에 menu 추가
        orderList.append(menu)
        print(f"{menu} 추가 완료")
    else:
        print("없는 메뉴입니다.")


# 실행 영역
print("D.Burger 셀프 주문 시스템입니다.")
while True:
    # 주문 타입 입력
    orderType = int(input("메뉴 타입을 번호로 입력하세요 (버거:1/음료:2/종료:3): "))
    # 주문 타입에 따라 버거 또는 음료 주문
    if orderType == 1:
        myBurger = input("추가할 버거:")
        orderBurger(myBurger)
    elif orderType == 2:
        myDrink = input("추가할 음료:")
        orderDrink(myDrink)
    # 주문 종료
    elif orderType == 3:
        print("-------------------------")
        print(f"주문 내역: {orderList}")
        print("주문을 종료합니다.")
        break