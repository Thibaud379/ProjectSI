from Utils import createScaler
from __future__ import division
from Adafruit_PCA9685 import PCA9685 as pwm

def setup():
    frequency = 50
    pwm.set_pwm_frequency(frequency)
    bitLength = 1000 / frequency / 4096
    servos   = []
    servo[0] = Servo(0, 180, 0.5, 2.5)
    servo[1] = Servo(1, 180, 0.5, 2)
    servo[2] = Servo(2, 180, 0.5, 2)
    servo[3] = Servo(3, 180, 0.7, 2.3)

def rotateServos(angles, debug = False):
    for servo,angle in (servos,angles):
        servo.rotate(angle, debug)
    
class Servo:
    def __init__(self, channel, angleMax, minPulse, maxPulse):
        self.angleMax = angleMax
        self.scaler   = createScaler(0,self.angleMax,minPulse,maxPulse)
        self.channel  = channel
        

    def rotate(self, angle, debug):
        if not 0<= angle <= self.angleMax:
            print("Error angle not in servo range (0 ~ "+str(self.angleMax)+" | "+str(angle)+")")
            return
        pulse = self.scaler(angle)
        bits  = pulse // bitLength
        pwm.set_pwm(self.channel, 0, int(bits))
        if debug:
            print("---Channel---")
            print(self.channel)
            print("---Angle & Pulse---")
            print(angle, pulse)
            print("---BitLength & Bits---")
            print(bitLength, bits)
            

setup()
