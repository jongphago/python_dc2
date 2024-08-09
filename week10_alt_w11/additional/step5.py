priceList = {
    "불고기버거": 3200,
    "새우버거": 4000,
    "치즈버거": 2800,
    "스프라이트": 1500,
    "우유": 1200,
    "콜라": 1500,
    "치즈스틱": 0,
}
totalPrice = 0
burgers = ["불고기버거", "새우버거", "치즈버거"]
drinks = ["스프라이트", "우유", "콜라"]
orderList = {}


# 함수 정의 영역
def order(type, menu):
    if menu in type:
        num = int(input("수량:"))
        if menu in orderList.keys():
            orderList[menu] += num
        else:
            orderList[menu] = num
        print("%s 추가 완료" % menu)
    else:

        print("없는 메뉴입니다.")

    print("현재 장바구니:", orderList)


def pay():
    global totalPrice

    print("주문 내역:", orderList)

    for myMenu in orderList.keys():
        totalPrice += priceList[myMenu] * orderList[myMenu]

    print("총 금액: %d원" % totalPrice)

    if totalPrice >= 15000:
        print("치즈스틱을 드립니다!")
        orderList["치즈스틱"] = 1
        print("주문 내역: ", orderList)


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
        pay()
        break
    else:
        print("다시 입력해 주세요.")
