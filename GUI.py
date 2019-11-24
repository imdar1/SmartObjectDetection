from tkinter import *
from component.FuncButtons import *
from component.ImageLayout import *
from component.TextBoxLayout import *

class RuleTre:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()


### MAIN LAYOUT ###
root = Tk()
root.title('Shape Detection')

## TOP FRAME ##
topFrame = Frame(root)
topFrame.pack(side=TOP)
sourceImage = ImageLayout(topFrame, side=LEFT, text="Source Image", headerInImage="Please Open an Image", textInImage="Click -> Open Image Button")
detectionImage = ImageLayout(topFrame, side=LEFT, text="Detection Image")

## BOTTOM FRAME ##
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
textBoxDetectionResult = TextBoxLayout(bottomFrame, side=LEFT, text="Detection Result")
textMatchedFacts = TextBoxLayout(bottomFrame, side=LEFT, text="Matched Facts")
textHitRules = TextBoxLayout(bottomFrame, side=LEFT, text="Hit Rules")

buttons = FuncButtons(topFrame, side=LEFT, sourceImage=sourceImage, detectionImage=detectionImage, textBoxDetectionResult=textBoxDetectionResult, textMatchedFacts=textMatchedFacts, textHitRules=textHitRules)

root.mainloop()
