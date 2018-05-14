import utils
from picamera import PiCamera
import numpy as np
from math import tan
from math import radians
from pprint import pprint

#---Defining a few constant and initialising the camera---

#The vertical angle of the camera's field of view
viewA = radians(48.8)
#The constant used to find the real size of the picture
sizeFactor = tan(viewA/2)

#Initialising the camera to take 512*512 pictures
camera = PiCamera()
camera.resolution = (512,512)

#Takes in the current arm's end position
#  and returns a position above the target
def getPos(pos, debug=False):
    #Initialise the image array
    image = np.empty((512 * 512 * 3), dtype=np.uint8)
    #Get an image from the camera and reshape the image array
    #  from a 1 to a 2 dimensionnal array
    camera.capture(image, 'bgr')
    image = image.reshape((512,512,3))
    #Get the possible circles in the image
    circles = utils.getCircles(image)

    #If none were found
    if circles is None:
        #print a warning
        print('[Warning] No target found')
        #keep the same position
        x=pos[0]
        z=pos[2]
	deltaX = 0
	deltaZ = 0
	circle = None
    #If there is at least one circle
    else:
        #Get the first circle in the list
        #  (the one with the most potential as a target)
        circle = circles[0][0][:2]
        #Compute the real size of the picture
        size = 2.0*float(pos[1])* sizeFactor
        #Get the circle's position on the image
	xImage = float(circle[0])
        zImage = float(circle[1])
        #Compute the real circle coordinates relative to the camera
        x = (xImage/512.0) * size
        z = (zImage/512.0) * size
        #Compute by how much the arm should move to be above th target
        deltaX = x - size/2
        deltaZ = z - size/2
    #Compute the new desired position
    newPos = [pos[0]+deltaX, pos[1], pos[2]+deltaZ]

    if debug:
        print("---Circle Array---")
        pprint(circles)
        print("---Circle chosen---")
        print(circle)
        print("---Positions---")
        print("Before:")
        pprint(pos)
        print("After:")
        pprint(newPos)
	print("---xImage & zImage---")
	print(xImage, zImage)
	print("---x & z---")
        print(x,z)
        print("---deltaX & deltaZ---")
        print(deltaX, deltaZ)
        
    return newPos
