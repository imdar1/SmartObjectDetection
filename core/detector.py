import numpy as np
import cv2
from math import sqrt

class Detector:
    def __init__(self, image_name):
        self.img = cv2.imread(image_name)
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        _,thresh = cv2.threshold(gray,127,255,1)

        _, contours, _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            self.approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)

            # Add approx to the set of edges
            self.edges = []
            for i in range (len(self.approx)):
                self.edges.append( [ self.approx[i][0][0], self.approx[i][0][1] ] )
            
    def detect_image(self):
        # Draw green lines for every edges
        line_thickness = 7
        count = len(self.edges)
        for i in range(count):
            cv2.line(self.img, (self.edges[i][0], self.edges[i][1]), (self.edges[(i+1) % count][0], self.edges[(i+1) % count][1]), (0,255,0), line_thickness)

        return self.img

    def get_slope(self,x1, y1, x2, y2):
        m = (y2-y1)/(x2-x1)
        return m

    def get_angle(self,x1, y1, vertex_x, vertex_y, x2, y2):
        a = np.array([x1, y1])
        b = np.array([vertex_x, vertex_y])
        c = np.array([x2, y2])

        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        rad = np.arccos(cosine_angle)
        return np.degrees(rad) # convert rad to degree
        

    def get_length(self,x1, y1, x2, y2):
        return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

    def get_all_degrees(self):
        degrees = []
        count = len(self.edges)
        for i in range(count):
            e1 = self.edges[(i-1) % count]
            vertex = self.edges[i]
            e2 = self.edges[(i+1) % count]
            degrees.append(self.get_angle(e1[0], e1[1], vertex[0], vertex[1], e2[0], e2[1]))
        
        return degrees

    def get_all_length(self):
        lengths = []
        count = len(self.edges)
        for i in range(count):
            p1 = self.edges[i]
            p2 = self.edges[(i+1) % count]
            lengths.append(self.get_length(p1[0], p1[1], p2[0], p2[1]))

        return lengths

    def get_all_slopes(self):
        slopes = []
        count = len(self.edges)
        for i in range(count):
            p1 = self.edges[i]
            p2 = self.edges[(i+1) % count]
            slopes.append(self.get_slope(p1[0], p1[1], p2[0], p2[1]))

        return slopes
    
    def get_edges_length(self):
        return len(self.edges)

    def get_all_edges(self):
        return self.edges