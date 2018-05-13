#A few useful and miscellaneous functions
import cv2
import numpy
from math import sqrt
import tinyik

#Defining the arm model used by the tinyik library
# to compute the inverse kinematic
arm = tinyik.Actuator(['y', [0., 0., 0.], 'x', [0., 1., 0.], 'x',[0.,1.,0.]])
arm.ee = [1,1,1]

#Takes an image as input and returns a list of possible circle found
def getCircles(image):
       #Blur the image to ease the detection of circles
       imageB = cv2.medianBlur(image,5)
       #Turn it into grayscale
       imageG = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)
       #Call the opencv library to find circles
       circles = cv2.HoughCircles(imageG,cv2.cv.CV_HOUGH_GRADIENT,1,100,param1=17,param2=8)
       return circles

#Computes the euclidian distance between two points
#  represented by their coordinates a & b in lists
def dist(a,b):
       #Create a list whose items are the difference
       #  between the two other lists's
       c = (a[x] - b[x] for x in range(len(a)))
       #Compute the sum of each item squared
       v=0
       for i in c:
              v += i**2
       #Return the square root
       return sqrt(v)

#A function used by the analytical programm
#  to measure the acuracy of a circle's position.
#The closer to 1 the output the more accurate
def getAccuracy(a,b):
       #Get the distance between the two coordinates
       d = dist(a,b)
       #Apply the formula 1-(value/maxValue)
       return 1-(d/710)

#Takes in a list and returns the average value of all its items
def getAvg(a):
       #Sum of all the items in the list
       t = 0
       for v in a:
              t+=v
       #Divide by the number of items
       return (t/len(a))

#Computes the inverse kinematics of the arm
#  and returns the servos angles in a list
def getAngles(pos, debug = False):
       #Sets the model arm position,
       #  thus telling the library to compute the angles of each servo
       arm.ee = pos
       if debug:
              print("---pos---")
              print(arm.ee)
              print("---angles---")
              print(arm.angles)
       #return the different angles
       return arm.angles
       
#Takes in input/output values bounds and returns a function
#  to map a value from the first interval to the other
def createScaler(inMin, inMax, outMin, outMax):
       #Creates a function using basic algebra to map a value
       #  from one range to another
       def scaler(value):
              return outMin + (value - inMin)*(float(outMax-outMin)/float(inMax-inMin))
       #Return the function
       return scaler
       

#---Tests of the diferent functions---
#
#image = cv2.imread('refs/ref2.png')
#file = open('refs/ref2.txt')
#refPos = eval(file.readline())
#circle = getCircle(image, 5, 40, 40)
#print(type(circle))
#if type(circle) is numpy.float64:
#       print('error')
#else:
#       print(circle[0][0])
#
#scaler = createScaler(0,100,-10,20)
#print(scaler(0))
#print(scaler(100))
#print(scaler(50))
