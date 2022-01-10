from os.path import basename, splitext
import tkinter as tk
import random
from tkinter.constants import COMMAND

class Appka(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Udělátko"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.varR = tk.IntVar()
        self.varG = tk.IntVar()
        self.varB = tk.IntVar()


        self.frameR = tk.Frame(self)
        self.frameR.pack()
        self.lblR = tk.Label(self.frameR, text = "R",fg = "#000000")
        self.lblR.pack(side = tk.LEFT, anchor = tk.S)
        self.scaleR = tk.Scale(self.frameR, from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, fg = "#ff0000", border = 2, variable = self.varR)
        self.scaleR.pack(side = tk.LEFT, anchor = tk.S)
        self.entryR = tk.Entry(self.frameR, width = 3, textvariable = self.varR)
        self.entryR.pack(side = tk.LEFT, anchor = tk.S)

        self.frameG = tk.Frame(self)
        self.frameG.pack()
        self.lblG = tk.Label(self.frameG, text = "G")
        self.lblG.pack(side = tk.LEFT, anchor = tk.S)
        self.scaleG = tk.Scale(self.frameG, from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, fg = "#00ff00", border = 2, variable = self.varG)
        self.scaleG.pack(side = tk.LEFT, anchor = tk.S)
        self.entryG = tk.Entry(self.frameG, width = 3, textvariable = self.varG)
        self.entryG.pack(side = tk.LEFT, anchor = tk.S)

        self.frameB = tk.Frame(self)
        self.frameB.pack()
        self.lblB = tk.Label(self.frameB, text = "B")
        self.lblB.pack(side = tk.LEFT, anchor = tk.S)
        self.scaleB = tk.Scale(self.frameB, from_ = 0, to = 255, orient = tk.HORIZONTAL, length = 256, fg = "#0000ff", border = 2, variable = self.varB)
        self.scaleB.pack(side = tk.LEFT, anchor = tk.S)
        self.entryB = tk.Entry(self.frameB, width = 3, textvariable = self.varB)
        self.entryB.pack(side = tk.LEFT, anchor = tk.S)
        
        self.canvasmain = tk.Canvas(width = 255, height = 255, background = "#000000")
        self.canvasmain.pack()
        self.varMain = tk.StringVar()
        self.entryMain = tk.Entry(self, textvariable=self.varMain,state="readonly",readonlybackground="#00ff00")
        self.canvasmain.bind("<Button-1>", self.mousehandler)
        self.entryMain.pack()
        self.varR.trace("w", self.change)
        self.varG.trace("w", self.change)
        self.varB.trace("w", self.change)

        
        self.frameMem = tk.Frame(self)
        self.frameMem.pack()
        self.canvasMem = []
        with open("barvy_last.txt","r") as f:
            for row in range(3):
                for column in range(7):
                    background = f.readline().rstrip("\n")
                    canvas = tk.Canvas(self.frameMem, width=50, height=50, background = background)
                    canvas.grid(row=row ,column=column)
                    canvas.bind("<Button-1>", self.mousehandler)
                    self.canvasMem.append(canvas.cget("background"))


    def mousehandler(self, event):
        if self.cget("cursor") != "pencil":
            self.config(cursor="pencil")
            self.color = event.widget.cget("background")
        elif self.cget("cursor") == "pencil":
            self.config(cursor="")
            event.widget.config(background=self.color)
        
        barva = event.widget["bg"]
        try:
            pozice = str(str(event.widget).split(".!")[2])
            pozice = pozice.replace("canvas", "", 1)
            if pozice == "":
                pozice = 1
            else:
                pozice = int(pozice)
            self.canvasMem[pozice - 1] = barva
        except:
            pass

    def change(self, var, index, event):
        r = self.scaleR.get()
        g = self.scaleG.get()
        b = self.scaleB.get()
        self.varR.set(r)
        self.varG.set(g)
        self.varB.set(b)
        colorstring = f"#{r:02x}{g:02x}{b:02x}"
        self.canvasmain.config(background = colorstring)
        self.varMain.set(colorstring)

    def quit(self, event = None):
        self.barvy_last()
        super().quit()

    def barvy_last(self, event = None):
        with open("barvy_last.txt", "w") as f:
            for i in range(len(self.canvasMem)):
                f.write(f"{self.canvasMem[i]}\n")

        
app = Appka()
app.mainloop()