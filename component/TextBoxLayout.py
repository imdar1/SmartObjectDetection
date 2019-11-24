from tkinter import *

class TextBoxLayout:
    def __init__(self, master, side=None, text="", hidden=False):
        self.frame = Frame(master)
        if side:
            self.frame.pack(side=side)
        else:
            self.frame.pack()

        self.scrollbar = Scrollbar(self.frame)
        self.textBox = Text(self.frame, height=20, width=30)

        self.labelTextBox = Label(self.frame, text=text)
        self.labelTextBox.pack()

        self.textBox.config(yscrollcommand=self.scrollbar.set, state=DISABLED)
        self.textBox.pack(side=LEFT, fill=Y)
        
        self.scrollbar.config(command=self.textBox.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        if hidden:
            self.hideTextBox()
        else:
            self.showTextBox()

    def insertTextLine(self, text):
        text = text + "\n" 
        self.textBox.config(state=NORMAL)
        self.textBox.delete("1.0", END)
        self.textBox.insert(END, text)
        self.textBox.config(state=DISABLED)
    
    def clearTextBox(self):
        self.textBox.delete("1.0", END)
        self.textBox.update()

    def showTextBox(self):
        self.labelTextBox.pack()
        self.textBox.pack(side=LEFT, fill=Y)
        self.scrollbar.pack(side=RIGHT, fill=Y)

    def hideTextBox(self):
        self.labelTextBox.pack_forget()
        self.textBox.pack_forget()
        self.scrollbar.pack_forget()