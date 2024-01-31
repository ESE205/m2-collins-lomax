import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
button=8
pin1=10
iteration=1
timecount=0
state="off"

start = time.time()

GPIO.setup(button,GPIO.IN)
GPIO.setup(pin1,GPIO.OUT,initial=GPIO.LOW)
t=int(input('For how many seconds would you like the program to run?'))
blinkrate=int(input('For how many seconds would you like the LED to blink?'))

DEBUG = False
if '-debug' in sys.argv:
	DEBUG = True

with open('data.txt', 'w') as data:
	while t>timecount:
		if GPIO.input(button):
			GPIO.output(pin1,1)
			state="ON"
			time.sleep(blinkrate)
			print(f'{time.time()-start}\t{state}')
			data.write(f'{time.time()-start}\t{state}\n')
			GPIO.output(pin1,0)
			state="OFF"
			time.sleep(blinkrate)
			data.write(f'{time.time()-start}\t{state}\n')
			print(f'{time.time()-start}\t{state}')
			timecount=timecount+2*blinkrate
			if DEBUG:
				print(f'{time.time()-start}\t{GPIO.output}\t{iteration}')
		else:
			data.write(f'{time.time()-start}\t{state}\n')
			print(f'{time.time()-start}\t{state}')
			timecount=timecount+blinkrate
			time.sleep(blinkrate)
			if DEBUG:
				print(f'{time.time()-start}\t{GPIO.output}\t{iteration}')
		iteration=iteration+1
GPIO.cleanup()
