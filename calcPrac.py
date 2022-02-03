import tkinter
from tkinter import *

root = Tk()
root.title("POG Calculator uwu")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

label_result = Label(root, width=25, height=2, text="", font=("arial",30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="black", bg="black").place(x=10,y=100)

root.mainloop()