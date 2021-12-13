#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Label, Button, Scale, HORIZONTAL, Canvas, LEFT, Entry, Frame, S
from typing import Text

# from tkinter import tt




class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "COlor mishmash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
###           R 
        self.frameR = Frame(self)
        self.frameR.pack()
        self.lblR = Label(self.frameR, text="R")
        self.lblR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(self.frameR, from_=0, to=255, orient=HORIZONTAL, length=600, command=self.change)
        self.scaleR.pack(side=LEFT, anchor=S)

        self.entryR = Entry(self.frameR, width=5)
        self.entryR.pack(side=LEFT, anchor=S)

###           G
        self.frameG = Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text="G")
        self.lblG.pack(side=LEFT, anchor=S)
        self.scaleG = Scale(self.frameG, from_=0, to=255, orient=HORIZONTAL, length=600, command=self.change)
        self.scaleG.pack(side=LEFT, anchor=S)

        self.entryG = Entry(self.frameG, width=5)
        self.entryG.pack(side=LEFT, anchor=S)

###           B
        self.frameB = Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text="B")
        self.lblB.pack(side=LEFT, anchor=S)
        self.scaleB = Scale(self.frameB, from_=0, to=255, orient=HORIZONTAL, length=600, command=self.change)
        self.scaleB.pack(side=LEFT, anchor=S)

        self.entryB = Entry(self.frameB, width=5)
        self.entryB.pack(side=LEFT, anchor=S)

        self.canvasmain = Canvas(width=600, height=100, background='#000000')
        self.canvasmain.pack()

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        
    def change(self, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.canvasmain.config(background=f'#{r:02x}{g:02x}{b:02x}')



    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
