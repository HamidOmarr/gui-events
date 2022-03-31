from tkinter import *
Window = Tk()


Window.counter = 0
def PlusCounter():
    Window.counter += 1
    Labels['text'] =  str(Window.counter)
    if Window.counter > 0:
        Window['background']='green'
    if Window.counter == 0:
        Window['background']='gray'

def MinCounter():
    Window.counter -= 1
    Labels['text'] =  str(Window.counter)
    if Window.counter < 0:
        Window['background']='red'
    if Window.counter == 0:
     Window['background']='gray'
def MuisHover(event):
    Window.config(bg='yellow')
def MuisLeave(event):
    if Window.counter == 0:
        Window.config(bg='gray')
    if Window.counter < 0:
        Window.config(bg='red')
    if Window.counter > 0:
        Window.config(bg='green')


Omhoog = Button(Window, text="Up", command=PlusCounter)
Omlaag = Button(Window, text="Down", command=MinCounter)
Labels = Label(Window, text="...")
Omhoog.pack(padx = 20,pady = 7)
Labels.pack(padx = 20,pady = 5)
Omlaag.pack(padx = 20,pady = 5)

Labels.bind("<Enter>", MuisHover)
Labels.bind("<Leave>", MuisLeave)

Window.mainloop()