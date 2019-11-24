from tkinter import *

class ImageLayout:
    def __init__(self, master, side=None, text="", headerInImage="", textInImage=""):
        frame = Frame(master)
        if side:
            frame.pack(side=side)
        else:
            frame.pack()

        self.labelImage = Label(frame, text=text)
        self.labelImage.pack()

        self.canvas = Canvas(frame, width=400, height=400, bg="white")
        self.header = self.canvas.create_text(200, 200, text=headerInImage, font=('Arial', 17, 'bold'))
        self.text = self.canvas.create_text(200, 225, text=textInImage, font=('Arial', 12, 'bold'))
        self.canvas.pack()