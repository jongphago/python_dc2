# 도형의 넓이를 구해주는 함수들을 구현해 봅시다.
def triangle(base, height):
    area = base * height / 2
    return area


def rectangle(width, height):
    area = width * height
    return area


def circle(radius):
    area = radius**2 * 3.14
    return area


while True:
    what = input("도형을 선택하세요(삼각형/사각형/원): ")
    if what == "삼각형":
        base = int(input("밑변: "))
        height = int(input("높이: "))
        print(f"넓이는 {(triangle(base, height))}입니다.")
    elif what == "사각형":
        width = int(input("가로: "))
        height = int(input("세로: "))
        print(f"넓이는 {(rectangle(width, height))}입니다.")
    elif what == "원":
        radius = int(input("반지름: "))
        print(f"넓이는 {(circle(radius))}입니다.")
    else:
        print("잘못 입력했습니다. ")
