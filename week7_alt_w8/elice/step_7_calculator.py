from tkinter import Tk, Label, Button

tk = Tk()

result = ""


def btn_click(value):
    global result

    if value == "=":
        result = None
    else:
        result = None
    lbl["text"] = None


lbl = Label(tk, text="0", height=5)
lbl.grid(row=0, columnspan=4)

txts = []
for index, txt in enumerate(txts):
    btn = None  # i
    btn  # grid를 사용하여 위젯 배치

txts = []
for index, txt in enumerate(txts):
    btn = None  # i
    btn  # grid를 사용하여 위젯 배치

txts = []
for index, txt in enumerate(txts):
    btn = None  # i
    btn  # grid를 사용하여 위젯 배치

for index, txt in zip([0, 2, 3], ["0", "=", "/"]):
    btn = None  # i
    btn  # grid를 사용하여 위젯 배치

tk.mainloop()
