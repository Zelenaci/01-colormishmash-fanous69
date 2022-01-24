#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import Label, Button, Scale, Canvas

from tkinter import HORIZONTAL, LEFT, Frame, Entry, Canvas, S, StringVar, IntVar
#dominik slehofer
# from tkinter import ttk

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "RGB"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.protocol("WM_DELETE_WINDOW", self.quit)




#red
        self.varR = IntVar()
       
        self.frameR= Frame(self)
        self.frameR.pack()#umístí do hlavního okna
        self.lblR = tk.Label(self.frameR, text="R")
        self.lblR.pack(side=LEFT, anchor=S)
        self.scaleR = Scale(self.frameR, from_=0, to=255, orient=HORIZONTAL, length=256,variable=self.varR)
        self.scaleR.pack()

        self.scaleR.pack(side=LEFT, anchor=S)
        self.entryR = Entry(self.frameR, width=5, textvariable=self.varR)
        self.entryR.pack(side=LEFT, anchor=S)






#grn
        self.varG = IntVar()
       
        self.frameG= Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text="G")
        self.lblG.pack(side=LEFT, anchor=S)
        self.scaleG = Scale(self.frameG, from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varG)
        self.scaleG.pack()

        self.scaleG.pack(side=LEFT, anchor=S)
        
        self.entryG = Entry(self.frameG, width=5, textvariable=self.varG)
        self.entryG.pack(side=LEFT, anchor=S)






#blue


        self.varB=IntVar()
       
        self.frameB= Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text="B")
        self.lblB.pack(side=LEFT, anchor=S)
        self.scaleB = Scale(self.frameB, from_=0, to=255, orient=HORIZONTAL, length=256, variable=self.varB)
        self.scaleB.pack()

        self.scaleB.pack(side=LEFT, anchor=S)
        self.entryB = Entry(self.frameB, width=5, textvariable=self.varB)
        self.entryB.pack(side=LEFT, anchor=S)



        self.canvasMain=Canvas(width=256, height=100, background="#000000")
        self.canvasMain.pack()
        self.canvasMain.bind( "<Button-1>", self.mousehandler)

        self.varMain=StringVar()
        self.entryMain = Entry(self, textvariable=self.varMain, state="readonly", readonlybackground="#f3f3f3",)
        self.entryMain.pack()


        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

        self.btn2 = tk.Button(self, text="About", command=self.quit)
        self.btn2.pack()


        self.varR.trace("w", self.change)
        self.varG.trace("w", self.change)
        self.varB.trace("w", self.change)


        self.frameMem =  Frame(self)
        self.frameMem.pack()
        self.canvasMem = []
        for row in range(3):
            for column  in range(7):
                canvas = Canvas(
                    self.frameMem, width=50, height=50, background="#abcdef"
                )
                canvas.grid(row=row, column=column)
                canvas.bind( "<Button-1>", self.mousehandler)

                self.canvasMem.append(canvas)
        
        self.colorLoad()

    
    def mousehandler(self, event):
        #print(dir(event))
        if self.cget("cursor") != "pencil":
            self.config(cursor = "pencil")
            self.color = event.widget.cget("background")
        elif self.cget("cursor") == "pencil":
            self.config(cursor="")
            event.widget.config(background=self.color)

            if event.widget is self.canvasMain:
                self.canvasColor2Slids(self.canvasMain)

    def change(self, var, index, mode):
        #self.lblG.config(text="ahoj")

        r = self.varR.get()
        g = self.varG.get()
        b = self.varB.get()

        color=f"#{r:02x}{g:02x}{b:02x}"

        self.canvasMain.config(background=color)#0 před 2 říká:vyplň prázdné místo nulami, 
        self.varMain.set(color)
      
    def canvasColor2Slids(self, canvas):
        color = canvas.cget("background")
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:], 16)
        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)
        self.change
    
    def colorSave(self):
        with open("colors.txt", "w") as f:
            f.write(self.canvasMain.cget("background") + "\n")
            for canvas in self.canvasMem:
                f.write(canvas.cget("background") + "\n")


    def colorLoad(self):
        with open("colors.txt", "r") as f:
          colorcode = f.readline().strip()
          self.canvasMain.config(background=colorcode)
          self.canvasColor2Slids(self.canvasMain)  

    def quit(self, event=None):
        self.colorSave()
        super().quit()



app = Application()
app.mainloop()