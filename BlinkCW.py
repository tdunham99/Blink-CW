import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

yellow = 6
green = 17
red = 27
button = 19

GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
	if GPIO.input(button) == False:
		GPIO.output(yellow, True)
		sleep(.25)
		GPIO.output(yellow, False)
		sleep(.5)
		GPIO.output(green, True)
		sleep(.25)
		GPIO.output(green, False)
		sleep(.5)
		GPIO.output(red, True)
		sleep(.25)
		GPIO.output(red, False)
	elif GPIO.input(button) == True:
		GPIO.output(yellow, False)
		GPIO.output(green, False)
		GPIO.output(red, False)

GPIO.cleanup()
