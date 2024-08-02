import random  # random 모듈을 불러옵니다.
from tkinter import Tk, Button, PhotoImage

tk = Tk()

buttons = {}
button_symbols = {}

symbols = []
for x in range(6):
    img = PhotoImage(file=f"week9_alt_w10/images/{x + 1}.png")
    symbols.append(img)
    symbols.append(img)

# TODO: symbols 리스트를 섞어줍니다.
random.shuffle


for i in range(3):
    for j in range(4):
        btn = Button(width=100, height=100)
        btn.grid(row=i, column=j)

        buttons[i, j] = btn
        button_symbols[i, j] = symbols.pop()
        buttons[i, j]["image"] = button_symbols[i, j]


tk.mainloop()
