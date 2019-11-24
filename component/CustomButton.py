from tkinter import *

class CustomButton:
    def __init__(self, master, text="Button", padx=10, pady=10, handler=None):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text=text, bg='white', 
            width=20, activebackground="#007AFF", activeforeground="white", bd=1)
        self.button.bind('<Button-1>', handler)
        self.button.pack(padx=padx, pady=pady)