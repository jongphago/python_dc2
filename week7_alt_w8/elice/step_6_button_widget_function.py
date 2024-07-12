from tkinter import Tk, Label, Button

tk = Tk()

counter = 0


def click():
    global counter
    counter += None
    lbl1["text"] = None


def reset():
    global counter
    counter = None
    lbl1["text"] = None


lbl1 = Label(tk, text="click count : " + str(counter))
lbl1.pack(side="left")

btn1 = Button(tk, text="click", command=click)
btn1.pack(side="left")

btn2 = Button(tk, text="reset", command=reset)
btn2.pack(side="left")

tk.mainloop()
