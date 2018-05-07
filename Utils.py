import cv2
import numpy
from math import sqrt

def getCircles(image, blur, p1, p2):
       imageB = cv2.medianBlur(image,blur)
       imageG = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)
       circles = cv2.HoughCircles(imageG,cv2.cv.CV_HOUGH_GRADIENT,1,100,param1=p1,param2=p2)
       return circles
	
def dist(a,b):
        c = (a[x] - b[x] for x in range(len(a)))
        v=0
        for i in c:
                v += i**2
        return sqrt(v)

def getAccuracy(a,b):
       d = dist(a,b)
       return 1-(d/710)

def getAvg(a):
       t = 0
       for v in a:
              t+=v
       return (t/len(a))

def createScaler(inMin, inMax, outMin, outMax):
       def scaler(value):
              return outMin + (value - inMin)*(float(outMax-outMin)/float(inMax-inMin))
       return scaler
       


##image = cv2.imread('refs/ref2.png')
##file = open('refs/ref2.txt')
##refPos = eval(file.readline())
##circle = getCircle(image, 5, 40, 40)
##print(type(circle))
##if type(circle) is numpy.float64:
##       print('error')
##else:
##       print(circle[0][0])
##
##scaler = createScaler(0,100,-10,20)
##print(scaler(0))
##print(scaler(100))
##print(scaler(50))
