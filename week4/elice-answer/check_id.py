userID = "dlab1004"


# 함수 정의
def checkID():
    print("사용자를 확인하겠습니다.")
    check = input("현재 아이디: ")
    if check == userID:
        return True
    else:
        return False


def changeID(newID):
    global userID
    if checkID():
        userID = newID
        print("아이디가 변경되었습니다.")
    else:
        print("잘못 입력하였습니다.")


# 실행 영역
print("<<어서오세요. 디랩 홈페이지입니다.>>")
changeID("daddy123")
print(userID)
