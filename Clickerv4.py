from tkinter import *
Window = Tk()
Window.counter = 0
Counterhelp = 0


def PlusCounter(event):
    global Counterhelp
    Counterhelp = 1
    Window.counter += 1
    Labels['text'] =  Window.counter
    if Window.counter > 0:
        Window['background']='green'
    if Window.counter == 0:
        Window['background']='gray'

def MinCounter(event):
    global Counterhelp
    Counterhelp = 2
    Window.counter -= 1
    Labels['text'] =  Window.counter
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

def DubbelClick(event):
    if Counterhelp == 1:
        Window.counter *= 3
        Counterhelp == 0
        Labels['text'] = Window.counter

    elif Counterhelp == 2:
        Window.counter /= 3
        Counterhelp == 0
        Labels['text'] = Window.counter



Omhoog = Button(Window, text="Up", command=PlusCounter)
Omlaag = Button(Window, text="Down", command=MinCounter)
Labels = Label(Window, text="0")
Omhoog.pack(padx = 20,pady = 7)
Labels.pack(padx = 20,pady = 5)
Omlaag.pack(padx = 20,pady = 5)

Labels.bind("<Enter>", MuisHover)
Labels.bind("<Leave>", MuisLeave)
Labels.bind('<Double-Button-1>',DubbelClick)
Window.bind('<space>',DubbelClick)
Window.bind('a',PlusCounter)
Window.bind('-',MinCounter)
     
Window.mainloop()