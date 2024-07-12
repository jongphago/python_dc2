from tkinter import *

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

btn = Button(tk, text="4", width=5)
btn.grid(row=2, column=0)
btn = Button(tk, text="5", width=5)
btn.grid(row=2, column=1)
btn = Button(tk, text="6", width=5)
btn.grid(row=2, column=2)
btn = Button(tk, text="-", width=5)
btn.grid(row=2, column=3)

btn = Button(tk, text="7", width=5)
btn.grid(row=3, column=0)
btn = Button(tk, text="8", width=5)
btn.grid(row=3, column=1)
btn = Button(tk, text="9", width=5)
btn.grid(row=3, column=2)
btn = Button(tk, text="*", width=5)
btn.grid(row=3, column=3)

btn = Button(tk, text="0", width=5)
btn.grid(row=4, column=0)
btn = Button(tk, text="=", width=5)
btn.grid(row=4, column=2)
btn = Button(tk, text="/", width=5)
btn.grid(row=4, column=3)

tk.mainloop()
