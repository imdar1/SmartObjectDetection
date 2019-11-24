from tkinter import *
from tkinter.filedialog import askopenfilename
from component.CustomButton import *
from PIL import ImageTk, Image
import math
import webbrowser

class FuncButtons:
    def __init__(self, master, side=None, sourceImage=None):
        frame = Frame(master)
        if side:
            frame.pack(side=side)
        else:
            frame.pack()

        self.sourceImage = sourceImage
        self.openImageButton = CustomButton(frame, text="Open Image", handler=self.openImageHandler)
        self.openRuleEditorButton = CustomButton(frame, text="Open Rule Editor", handler=self.openRuleEditorHandler)
        self.showRulesButton = CustomButton(frame, text="Show Rules", handler=self.showRulesHandler)
        self.showFactsButton = CustomButton(frame, text="Show Facts", handler=self.showFactsHandler)

    def openImageHandler(self, event):
        filename = askopenfilename(title="Choose an image")
        self.sourceImage.canvas.delete(ALL)
        image = Image.open(filename)
        ratio = min(400/image.height, 400/image.width)
        image = image.resize((math.ceil(image.height * ratio), math.ceil(image.width * ratio)), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.sourceImage.canvas.create_image(200, 200, image=self.photo)

    def openRuleEditorHandler(self, event):
        webbrowser.open("rules.clp")

    def showRulesHandler(self, event):
        print('Show Rules')

    def showFactsHandler(self, event):
        print('Show Facts')