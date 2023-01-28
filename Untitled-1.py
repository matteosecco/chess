from tkinter import *

root = Tk()

a = Button(root)
a.pack(side=LEFT)
b = Button(root)

def prova(self):
    print("ciao")

b.pack(side=RIGHT)


root.bind("s", prova)
root.mainloop()