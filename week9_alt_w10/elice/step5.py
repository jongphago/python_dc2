import time  # time 모듈을 import 합니다.
import random
from tkinter import Tk, Button, PhotoImage, DISABLED

tk = Tk()

buttons = {}
button_symbols = {}

symbols = []

for x in range(6):
    img = PhotoImage(file=f"week9_alt_w10/images/{x + 1}.png")
    symbols.append(img)
    symbols.append(img)

random.shuffle(symbols)

# TODO: first, preX, preY 변수 선언
first = True
preX = 0
preY = 0

# TODO: empty_img 변수 선언
empty_img = None


# TODO: show_symbol 함수 구현
def show_symbol(x, y):
    global first
    global preX, preY

    # 윈도우 창에 보여지는 부분
    buttons[x, y]["image"] = button_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:  # 처음일 때
        preX = x
        preY = y
        first = False
    elif preX != x or preY != y:  # 두번째일 때 처음과 다른 곳을 눌렀다면
        # 처음 눌렀던 곳과 이미지가 다르다면
        if buttons[preX, preY]["image"] != buttons[x, y]["image"]:
            time.sleep(0.5)
            buttons[preX, preY]["image"] = empty_img
            buttons[x, y]["image"] = empty_img
        else:  # 처음 눌렀던 곳과 이미지가 같다면 함수가 실행되지 않도록
            buttons[preX, preY]["command"] = DISABLED
            buttons[x, y]["command"] = DISABLED
        # 처음으로 돌아가기
        first = True


for i in range(3):
    for j in range(4):
        # TODO: command 매개변수에 람다 함수를 사용하여 show_symbol 함수를 호출
        btn = Button(width=100, height=100, command=None)
        btn.grid(row=i, column=j)

        buttons[i, j] = btn
        button_symbols[i, j] = symbols.pop()
        # TODO: 버튼 이미지를 empty_img로 설정
        buttons[i, j]["image"] = None


tk.mainloop()
