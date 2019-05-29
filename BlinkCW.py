import RPi.GPIO as GPIO
from time import sleep
from builtins import False

GPIO.setmode(BCM)

yellow = 6
button = 26

GPIO.setup(yellow, GPIO.out)
GPIO.setup(button, GPIO.IN)

while True:
    if GPIO.input(button) == False:
        GPIO.output(yellow, True)
    else:
        GPIO.output(yellow, False)

GPIO.cleanup()