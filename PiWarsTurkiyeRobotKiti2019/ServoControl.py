from time import sleep
import RPi.GPIO as GPIO
from threading import Thread

class ServoKontrol:
    
    def __init__(self, pin=35, GPIOSetup = GPIO.BOARD):
        GPIO.setmode(GPIOSetup)
        
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.pin = pin
        self.targetAngle = 90
        self.currentAngle = 90
        self.hasSlept = True
        self.isContinous = False

    
    def setToContinous(self):
        self.isContinous = True
        GPIO.output(self.pin, True)
    
    def setToNotContinous(self):
        self.isContinous = False
        GPIO.output(self.pin, False)
    
    def __notContinousActual__(self):
        signalLength = self.targetAngle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(signalLength)

        deltaAngle = abs(self.targetAngle - self.currentAngle)
        requiredSleep = deltaAngle / 150
        sleep(requiredSleep)  # experimental value
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.currentAngle = self.targetAngle
        self.hasSlept = True
    
    def __continousActual__(self, angle):
        duty = angle / 18 + 2
        self.pwm.ChangeDutyCycle(duty)
    
    def setAngle(self, angle):

        self.targetAngle = angle

        if self.isContinous:
            self.__continousActual__(self.targetAngle)
        elif self.hasSlept and (self.currentAngle is not self.targetAngle):
            self.hasSlept = False
            
            Thread(target=self.__notContinousActual__(), args=()).start()
