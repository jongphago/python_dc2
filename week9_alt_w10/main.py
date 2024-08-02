import time
import random
from tkinter import *

tk = Tk()

buttons = {}
button_symbols = {}

symbols = []

for x in range(6):
    img = PhotoImage(file=f"week9_alt_w10/images/{x + 1}.png")
    symbols.append(img)
    symbols.append(img)

random.shuffle(symbols)

first = True  # True:첫번째, False:두번째
preX = 0
preY = 0

empty_img = PhotoImage(file="week9_alt_w10/images/empty.png")


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
        if (
            buttons[preX, preY]["image"] != buttons[x, y]["image"]
        ):  # 처음 눌렀던 곳과 이미지가 다르다면
            time.sleep(0.5)
            buttons[preX, preY]["image"] = empty_img
            buttons[x, y]["image"] = empty_img
        else:  # 처음 눌렀던 곳과 텍스트가 같다면 함수가 실행되지 않도록
            buttons[preX, preY]["command"] = DISABLED
            buttons[x, y]["command"] = DISABLED
        first = True


for x in range(3):
    for y in range(4):
        btn = Button(width=100, height=100, command=lambda x=x, y=y: show_symbol(x, y))
        btn.grid(row=x, column=y)

        buttons[x, y] = btn
        button_symbols[x, y] = symbols.pop()
        buttons[x, y]["image"] = empty_img

tk.mainloop()
