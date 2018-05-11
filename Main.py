from Vision import getAngles
from ServoHandler import rotateServos
from time import sleep
from Utils import getAngles
debug = input("Debug ?(True/False):")
repos =[0,0.2,0.3]
rotateServos(getAngles(repos),debug)
pos = repos
while True:
    newPos = Vision.getPos(pos, debug)
    rotateServos(getAngles(pos), debug)
    sleep(1)
