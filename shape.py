import numpy as np
import cv2

img = cv2.imread('square..gif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

image, contours,h = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==5:
        print( "pentagon" )
        # cv2.line(img,(approx[0][0][0],approx[0][0][1]),(approx[4][0][0],approx[4][0][1]),(0,0,255),2)
    elif len(approx)==3:
        print ("triangle")
    elif len(approx)==4:
        print ("square")
    elif len(approx) == 6:
        print('heksagon')
        # cv2.drawContours(img,[cnt],0,(0,255,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()