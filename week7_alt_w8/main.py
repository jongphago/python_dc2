from tkinter import Tk, Button

tk = Tk()

for index, i in enumerate(range(5)):
    btn = Button(tk, text=str(i))
    btn.grid(row=0, column=index)
    
tk.mainloop()
