from tkinter import Tk, Label, Button


tk = Tk()

lbl = Label(tk, text="0", height=5)
lbl.grid(row=0, columnspan=4)

btn = Button(tk, text="1", width=5)
btn.grid(row=1, column=0)
btn = Button(tk, text="2", width=5)
btn.grid(row=1, column=1)
btn = Button(tk, text="3", width=5)
btn.grid(row=1, column=2)
btn = Button(tk, text="+", width=5)
btn.grid(row=1, column=3)

btn = None  # 4
btn  # grid를 사용하여 위젯 배치
btn = None  # 5
btn  # grid를 사용하여 위젯 배치
btn = None  # 6
btn  # grid를 사용하여 위젯 배치
btn = None  # -
btn  # grid를 사용하여 위젯 배치

for index, txt in enumerate(["7", "8", "9", "*"]):
    btn = None  # i
    btn  # grid를 사용하여 위젯 배치

for index, txt in zip([0, 2, 3], ["0", "=", "/"]):
    btn = None  # i
    btn  # grid를 사용하여 위젯 배치

tk.mainloop()
