import numpy as np
import cv2

def get_slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m

def get_angle(x1, y1, vertex_x, vertex_y, x2, y2):
    a = np.array([x1, y1])
    b = np.array([vertex_x, vertex_y])
    c = np.array([x2, y2])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    rad = np.arccos(cosine_angle)
    return np.degrees(rad) # convert rad to degree
    

def get_length(x1, y1, x2, y2):
    return sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

def get_all_degrees(edges):
    degrees = []
    count = len(edges)
    for i in range(count):
        e1 = edges[(i-1) % count]
        vertex = edges[i]
        e2 = edges[(i+1) % count]
        degrees.append(get_angle(e1[0], e1[0], vertex[0], vertex[1], e2[0], e2[1]))
    
    return degrees

def get_all_length(edges):
    lengths = []
    count = len(edges)
    for i in range(count):
        p1 = edges[i]
        p2 = edges[(i+1) % count]
        degrees.append(get_length(p1[0], p1[1], p2[0], p2[1]))

    return lengths

def get_all_slopes(edges):
    slopes = []
    count = len(edges)
    for i in range(count):
        p1 = edges[i]
        p2 = edges[(i+1) % count]
        degrees.append(get_slope(p1[0], p1[1], p2[0], p2[1]))

    return slopes

img = cv2.imread('square.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

image, contours,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)

    # Add approx to the set of edges
    edges = []
    for i in range (len(approx)):
        edges.append( [ approx[i][0][0], approx[i][0][1] ] )

    # cv2.drawContours(img, [approx], 0, (0), 5)

    if len(approx)==5:
        print( "pentagon" )

    elif len(approx)==3:
        print ("triangle")

    elif len(approx)==4:
        print ("square")
        # Draw predicted shape
        lineThickness = 2
        for i in range(4):
            cv2.line(img, (approx[i][0][0], approx[i][0][1]), (approx[(i+1)%4][0][0], approx[(i+1)%4][0][1]), (0,255,0), lineThickness)
    
    elif len(approx) == 6:
        print('heksagon')
        lineThickness = 2
        for i in range(6):
            print(approx[i])
            cv2.line(img, (approx[i][0][0], approx[i][0][1]), (approx[(i+1)%6][0][0], approx[(i+1)%6][0][1]), (0,255,0), lineThickness)
        # cv2.drawContours(img,[cnt],0,(0,255,255),-1)
# cv2.imshow('img',img)
cv2.imshow('halo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()