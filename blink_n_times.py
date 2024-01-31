import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)

ITER_COUNT = 15  
pin1 = 10
switch=8
GPIO.setup(switch,GPIO.IN)
GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   
check=1

n=5

while(check):
	if(GPIO.input(switch)):

		n=int(input('How many times would you like the LED to blink?'))


		for x in range(n): # Run n times
			GPIO.output(pin1, True)   # Turn on
			sleep(1)                  # Sleep for 1 second
			GPIO.output(pin1, False)  # Turn off
			sleep(1)                  # Sleep for 1 second
		check=0


GPIO.cleanup()
