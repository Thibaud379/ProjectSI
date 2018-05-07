from Vision import getAngles
from ServoHandler import rotateServos
from time import sleep
pos =[0,0.27,0]
while True:
    (angles,pos) = Vision.getAngles(pos, True)
    rotateServos(angles, True)
    sleep(1)
