from tkinter import *

tk = Tk()


# TODO: Button 객체 3x4 생성
for i in range(3):
    for j in range(4):
        btn = Button(width=100, height=100)
        btn.grid(row=i, column=j)


tk.mainloop()
