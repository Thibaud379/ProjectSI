from Utils import createScaler
from __future__ import division
from Adafruit_PCA9685 import PCA9685 as pwm

#Creates Servo() instances with the project's parameters
#and sets the PWM's frequency
def setup():
    frequency = 50
    pwm.set_pwm_frequency(frequency)
    bitLength = 1000 / frequency / 4096
    #Creating an array with the 4 servo's parameters
    servos   = []
    servo[0] = Servo(0, 180, 0.5, 2.5)
    servo[1] = Servo(1, 180, 0.5, 2)
    servo[2] = Servo(2, 180, 0.5, 2)
    servo[3] = Servo(3, 180, 0.7, 2.3)

#Calls the rotate function of each servo with the right angle
def rotateServos(angles, debug = False):
    for servo,angle in (servos,angles):
        servo.rotate(angle, debug)

#A class defining a servo object to simplify using them
class Servo:

    #Init function which takes in all the required servo parameters 
    def __init__(self, channel, angleMax, minPulse, maxPulse):
        self.angleMax = angleMax
        self.scaler   = createScaler(0,self.angleMax,minPulse,maxPulse)
        self.channel  = channel
        
    #A function responsible for rotating a servo to a given angle
    def rotate(self, angle, debug):
        #Checks if the angle asked is in the servo's range
        if not 0<= angle <= self.angleMax:
            print("[Error] Angle not in servo range (0 ~ "+str(self.angleMax)+" | "+str(angle)+")")
            return None
        #Compute the pulse length in ms from the angle value
        pulse = self.scaler(angle)
        #Determine the equivalent in bits
        bits  = pulse // bitLength
        #Tells the servo to rotate to that angle
        pwm.set_pwm(self.channel, 0, int(bits))
        if debug:
            print("---Channel---")
            print(self.channel)
            print("---Angle & Pulse---")
            print(angle, pulse)
            print("---BitLength & Bits---")
            print(bitLength, bits)
            
#When this file is imported in the main programm, it calls the setup() function
setup()
