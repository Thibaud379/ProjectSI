#A very basic programm to test the code
from Vision import getAngles
from ServoHandler import rotateServos
from time import sleep
from Utils import getAngles

debug = input("Debug ?(True/False):")
rest =[0,0.2,0.3]
rotateServos(getAngles(rest),debug)
pos = rest
while True:
    newPos = Vision.getPos(pos, debug)
    rotateServos(getAngles(newPos), debug)
    sleep(1)
