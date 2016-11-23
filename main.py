from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Simple Window")
root.geometry("600x400")

def btnPressed():
    messagebox.showinfo("Say Hello", "Hello World!")


btn = Button(root, text="Start Now", command=btnPressed)
btn.place(x=250, y=30)

lbl = Label(root, text="Start Generating SIPs?", font=("Helvetica", 14), justify=LEFT)
lbl.place(x=20, y=30)

root.mainloop()