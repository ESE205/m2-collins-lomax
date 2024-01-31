import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
pin1=10
switch=8
GPIO.setup(switch,GPIO.IN)
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)

while(1):
	if(GPIO.input(switch)):
		GPIO.output(pin1, 1)
	#if(GPIO.input(switch)==0)
	else:
		GPIO.output(pin1,0)
GPIO.cleanup()
