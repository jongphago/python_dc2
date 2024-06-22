userID: str = "dlab1004"


def check_id(user_id: str) -> bool:
    check: str = input("아이디를 입력하세요: ")
    is_same = check == user_id
    if is_same:
        return True
    else:
        return False


def change_id(user_id: str, new_id: str) -> None:
    checked: bool = check_id(user_id=user_id)
    if checked:
        print("Yes")
        return new_id
    else:
        print("No")
        return None


new_id = change_id(user_id=userID, new_id="daddy123")
userID = new_id
print(userID)
