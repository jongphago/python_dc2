from tkinter import *

tk = Tk()

# TODO: buttons, button_symbols 변수 선언
buttons = {}
button_symbols = {}

# TODO: symbols 변수 선언
symbols = []
for x in range(6):
    img = PhotoImage(file=f"week9_alt_w10/images/{x + 1}.png")
    symbols.append(img)
    symbols.append(img)


for i in range(3):
    for j in range(4):
        btn = Button(width=100, height=100)
        btn.grid(row=i, column=j)

        # TODO: buttons, button_symbols에 버튼과 이미지 추가
        buttons[i, j] = btn
        button_symbols[i, j] = symbols.pop()
        buttons[i, j]["image"] = button_symbols[i, j]


tk.mainloop()
