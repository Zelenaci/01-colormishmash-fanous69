#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Label, Button, Scale, HORIZONTAL, Canvas
from typing import Text

# from tkinter import ttk




class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "COlor mishmash"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.lblR = tk.Label(self, text="R")
        self.lblR.pack()
        self.scaleR = Scale(from_=0, to=255, orient=HORIZONTAL, length=600, command=self.change)
        self.scaleR.pack()

        self.lblG = tk.Label(self, text="G")
        self.lblG.pack()
        self.scaleG = Scale(from_=0, to=255, orient=HORIZONTAL, length=600)
        self.scaleG.pack()

        self.lblB = tk.Label(self, text="B")
        self.lblB.pack()
        self.scaleB = Scale(from_=0, to=255, orient=HORIZONTAL, length=600)
        self.scaleB.pack()

        self.canvasmain = Canvas(width=600, height=100, background='#000000')
        self.canvasmain.pack()

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        
    def change(self, event):
        self.lblG.config(text='ahoj')

        r = scaleR.get()
        g = scaleG.get()
        b = scaleB.get()
        self.canvasmain.config(background=f'#{r}{g}{b}')


    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
