sandwich = ["계란", "양상추", "치즈", "토마토"]
toppingList = ["미트볼", "베이컨", "새우", "양파", "참치"]


# 함수 정의
def order(*topping):  # 가변인자 사용
    myMenu = []
    # myMenu에 기본 재료 추가, extend() 함수 사용
    pass

    for t in topping:
        if t in toppingList:
            # myMenu에 토핑 추가, append() 함수 사용
            pass
        else:
            print("{}: 없는 토핑입니다.".format(t))
    print("주문이 접수되었습니다.")
    print("재료: ", myMenu)


order("새우", "오이")
print(sandwich)

# 실행 영역
print("디랩 샌드위치의 기본 재료입니다.:", sandwich)
print("아래 토핑 중 추가할 수 있습니다.")
print(toppingList)
print("-------------------------------------------------")
