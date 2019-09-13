from time import sleep, time
import RPi.GPIO as GPIO
from threading import Thread

class UltrasonikSensoru:

    def __init__(self, echo, trig, setup=GPIO.BOARD):

        self.echo = echo
        self.trig = trig

        self.time = 0

        self.distance = list()
        self.instantenousMeasurement = 0

        GPIO.setmode(setup)

        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        GPIO.output(trig, False)

    def startMeasuring(self):

        Thread(target=self.__measureDistance__, args=()).start()
        sleep(0.2)

    def readDistance(self):
        return self.distance[8], self.instantenousMeasurement

    def __measureDistance__(self):

        while True:
            GPIO.output(self.trig, True)
            sleep(0.0001)
            GPIO.output(self.trig, False)

            signalStart = time()
            healthyMeasurement = 1

            while GPIO.input(self.echo) == 0:
                if abs(signalStart - time()) > 0.03:
                    healthyMeasurement = 0
                    break

            # save time of arrival
            while GPIO.input(self.echo) == 1 and healthyMeasurement:
                signalEnd = time()

            if healthyMeasurement:
                self.time = signalEnd - signalStart
                self.instantenousMeasurement = self.time * 17150
                self.distance.append(self.instantenousMeasurement)
                self.distance.sort()
                if len(self.distance) > 16:
                    self.distance.pop()
                    self.distance.pop(0)

