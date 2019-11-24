from tkinter import *
from tkinter.filedialog import askopenfilename
from component.CustomButton import *
from PIL import ImageTk, Image
from core.detector import Detector
from core.core import Core
import math
import webbrowser

class FuncButtons:
    def __init__(self, master, side=None, sourceImage=None, detectionImage=None, textBoxDetectionResult=None, textMatchedFacts=None, textHitRules = None):
        frame = Frame(master)
        if side:
            frame.pack(side=side)
        else:
            frame.pack()

        self.sourceImage = sourceImage
        self.detectionImage = detectionImage
        self.textBoxDetectionResult=textBoxDetectionResult
        self.textMatchedFacts=textMatchedFacts
        self.textHitRules = textHitRules
        self.openImageButton = CustomButton(frame, text="Open Image", handler=self.openImageHandler)
        self.openRuleEditorButton = CustomButton(frame, text="Open Rule Editor", handler=self.openRuleEditorHandler)
        self.showRulesButton = CustomButton(frame, text="Show Rules", handler=self.showRulesHandler)
        self.showFactsButton = CustomButton(frame, text="Show Facts", handler=self.showFactsHandler)

    def openImageHandler(self, event):
        filename = askopenfilename(title="Choose an image")
        self.sourceImage.canvas.delete(ALL)
        img = Image.open(filename)
        basewidth = 400
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img)
        self.sourceImage.canvas.create_image(200, 200, image=self.photo)
        self.detector = Detector(filename)
        img = Image.fromarray(self.detector.detect_image())
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        self.photo_result = ImageTk.PhotoImage(img)
        self.detectionImage.canvas.create_image(200, 200, image=self.photo_result)
        self.initDetector()

    def initDetector(self):
        fact_templates = [
            'sisi', 'jumlahSisiSama', 'sudutTumpul', 'sudutLancip', 'sudutSiku',
            'jumlahPasanganSejajar', 'sepasangSudutSama', 'maksXSiku', 'minXSiku', 'jumlahSudutSama'  
        ]
        fact_results = []
        delta = 5

        fact_results.append(self.detector.get_edges_length())

        # Sisi
        lengths = self.detector.get_all_length()

        # jumlah sisi sama
        count = 0
        for i in range(len(lengths)):
            temp_count = 0
            for j in range (len(lengths)):
                if (lengths[i] >= lengths[j]-delta and lengths[i] <= lengths[j] + delta):
                    temp_count += 1
            if temp_count > count:
                count = temp_count
        fact_results.append(count)

        degrees = self.detector.get_all_degrees()
        count_tumpul = 0
        count_siku = 0
        count_lancip = 0
        for degree in degrees:
            if (degree > 90-delta and degree < 90+delta):
                count_siku += 1
            elif (degree <= 90-delta):
                count_lancip += 1
            else:
                count_tumpul += 1
        # Sudut tumpul
        fact_results.append(count_tumpul)
        # Sudut lancip
        fact_results.append(count_lancip)
        # Sudut Siku
        fact_results.append(count_siku)

        # jumlahPasanganSejajar
        slopes = self.detector.get_all_slopes()
        count = 0
        forbidden_index = []
        for i in range (len(slopes)):
            for j in range(i+1, len(slopes)):
                if (slopes[i] >= slopes[j] - delta and slopes[i] <= slopes[j] + delta  and i not in forbidden_index and j not in forbidden_index):
                    count += 1
                    forbidden_index.append(i)
                    forbidden_index.append(j)
        fact_results.append(count)

        # Sepasang sudut sama
        count = 0
        forbidden_index = []
        for i in range (len(degrees)):
            for j in range(i+1, len(degrees)):
                if (degrees[i]  >= degrees[j] - delta and degrees[i] <= degrees[j] + delta and i not in forbidden_index and j not in forbidden_index):
                    count += 1
                    forbidden_index.append(i)
                    forbidden_index.append(j)
        fact_results.append(count)

        # maksXsiku
        edges = self.detector.get_all_edges()
        max_index = 0
        min_index = 0
        for i in range(len(edges)):
            if (edges[i][0] > edges[max_index][0]):
                max_index = i
            if (edges[i][0] < edges[min_index][0]):
                min_index = i
        if (degrees[max_index] > 90-delta and degrees[max_index] < 90+delta):
            fact_results.append('true')
        else:
            fact_results.append('false')

        #minXsiku
        if (degrees[min_index] > 90-delta and degrees[min_index] < 90+delta):
            fact_results.append('true')
        else:
            fact_results.append('false')

        # jumlahsudutsama
        count = 0
        for i in range(len(degrees)):
            temp_count = 0
            for j in range (len(degrees)):
                if (degrees[i] == degrees[j]):
                    temp_count += 1
            if temp_count > count:
                count = temp_count
        fact_results.append(count)

        core = Core('rules.clp')
        for i in range(10):
            fact = '('+str(fact_templates[i])+' '+str(fact_results[i])+')'
            core.assert_fact(fact)

        # Run and get hit rules
        hit_rules = core.get_hit_rules()

        # Get results
        object_result = core.get_results()

        # Get all matched facts
        facts = core.get_matched_facts()


        # print(hit_rules)
        # print(str(object_result))
        # print(facts)
        # Write to text box
        for hit_rule in hit_rules:
            self.textHitRules.insertTextLine(hit_rule)
        self.textBoxDetectionResult.insertTextLine(object_result)
        for fact in facts:
            self.textMatchedFacts.insertTextLine(fact)


    def openRuleEditorHandler(self, event):
        webbrowser.open("rules.clp")

    def showRulesHandler(self, event):
        print('Show Rules')

    def showFactsHandler(self, event):
        print('Show Facts')