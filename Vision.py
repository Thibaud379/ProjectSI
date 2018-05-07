import utils
from picamera import PiCamera
import tinyik
import numpy as np
from math import tan
from math import radians
from pprint import pprint

blur   = 5
param1 = 17
param2 = 8
heigthA = radians(48.8)
camera = PiCamera()
camera.resolution = (512,512)
camera.start_preview()
arm = tinyik.Actuator(['y', [0., 0., 0.], 'x', [0., 1., 0.], 'x',[0.,1.,0.]])

def getAngles(pos, debug=False):
        image = np.empty((512 * 512 * 3), dtype=np.uint8)
        camera.capture(image, 'bgr')
        image = image.reshape((512,512,3))
	circles = utils.getCircles(image, blur, param1, param2)
	if circles is None:
                print('No target found')
                x=pos[0]
                z=pos[2]
		deltaX = 0
		deltaZ = 0
		circle =None
        else:
            circle = circles[0][0][:2]
            size = 2.0*float(pos[1])*tan(heigthA/2)
            print(size)
	    xImage = float(circle[0])
            zImage = float(circle[1])
            x = (xImage/512.0) * size
            z = (zImage/512.0) * size
            deltaX = x - size/2
            deltaZ = z - size/2
	newPos = [pos[0]+deltaX, pos[1], pos[2]+deltaZ]
        arm.ee = newPos
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
            print("---Angle Array---")
            pprint(arm.angles)
        return (arm.angles, newPos)
