from tkinter import *
import tkinter
import time
import random
from tkinter.messagebox import askyesno

Window = Tk()
Window.title('Simple FPS Trainer')
Window.geometry('300x300')
Knoppenlist = ['w','a','s','d','<space>','<Double-Button>','<Button>','<Triple-Button>']

def Labeltext(event):
    for x in range(30,-1, -1):
        LabelTijd['text'] = 'Tijd:' , x
        Window.update()
        time.sleep(1)
        Startknop.pack_forget()
        Buttonknop.pack(padx= 20, pady= 7)
    if x <= 0:
        YesorNo = askyesno(message='Afsluiten?')
    if YesorNo:
        Window.destroy()
    
def ButtonDing(event):
    Buttonknop['text'] = random.choice(Knoppenlist)
    if Window['text'] == '<space>':
        Window.bind('<space>')
        Window.unbind('<Button>')

    # Buttonknop.unbind('<Button>')
    # Buttonknop.bind('<space>')






Buttonknop = Button(Window,text='   ')
Startknop = Button(Window,text='Start!')
LabelTijd = Label(Window, text='Tijd:  ')
LabelTijd.pack(padx = 20,pady = 7)
Buttonknop.pack_forget()
Startknop.pack(padx= 20, pady= 7)
Window.bind('<Button>',ButtonDing)
Window.bind('1', Labeltext)



Window.mainloop()