burgers = ["불고기버거", "새우버거", "치즈버거"]
drinks = ["스프라이트", "우유", "콜라"]
orderList = {}

# priceList, totalPrice를 정의하여 주문한 메뉴의 가격을 저장하고, 총 금액을 계산하는 pay 함수를 정의합니다.
totalPrice = None
priceList = {
    "불고기버거": 3200,
    "새우버거": 4000,
    "치즈버거": 2800,
    "스프라이트": 1500,
    "우유": 1200,
    "콜라": 1500,
    "치즈스틱": 0,
}


def order(type, menu):
    if menu in type:
        num = int(input("수량:"))
        if menu in orderList.keys():
            orderList[menu] += num
        else:
            orderList[menu] = num
        print(f"{menu} 추가 완료")
    else:
        print("없는 메뉴입니다.")

    print("현재 장바구니:", orderList)


# pay 함수를 정의하여 주문 내역을 출력하고, 총 금액을 계산합니다.
def pay():
    global totalPrice

    print("주문 내역:", orderList)
    # 주문한 메뉴의 가격을 계산하여 totalPrice에 더합니다.
    for myMenu in orderList.keys():
        totalPrice += None

    print("총 금액: %d원" % totalPrice)


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
        print("-------------------------")
        print("주문을 종료합니다.")
        print("주문 내역과 총 금액을 확인해 주세요.")
        # pay 함수를 호출하여 주문 내역과 총 금액을 출력합니다.
        pay()
        break
    else:
        print("다시 입력해 주세요.")
