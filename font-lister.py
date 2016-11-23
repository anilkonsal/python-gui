from tkinter import *
from tkinter import font

def refresh_items(text, iy):
    for item in fonts:
        lbl = Label(root, text=text + '  - ' + item, font=(item,20), justify=LEFT)
        lbl.place(x=20, y=iy)
        iy += 40

def btnPressed():
    refresh_items(e.get(), 50)


root = Tk()
root.title("Fonts Lister")
root.geometry("800x600")


fonts=list(font.families())
fonts.sort()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

e = Entry(root, width=75)
e.place(x=10, y=10)

btn = Button(root, text="Update", command=btnPressed)
btn.place(x=450, y=10)



iy = 50


refresh_items('Hello World', iy)
root.mainloop()