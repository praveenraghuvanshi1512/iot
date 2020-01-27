import RPi.GPIO as GPIOEX
import time

class GPIOEX:
    ''' Manages GPIO connection and behavior
    https://www.instructables.com/id/Raspberry-Pi-LED-Blink/'''
    def blinkLed(self):
        print('**** GPIOEX::Person Detected')
        print('LED On')
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        print('LED Off')
        GPIO.output(18, GPIO.LOW)

    def initialize(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18, GPIO.OUT)

gpio = GPIOEX()
gpio.blinkLed()