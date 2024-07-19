from tkinter import Tk, Label, Entry, Button


tk = Tk()


lbl = Label(tk, text="이름")    
lbl.grid(row=0, column=0)

txt = Entry(tk)
txt.grid(row=0, column=1)

btn = Button(tk, text="ok")
btn.grid(row=1, column=1)

tk.mainloop()
