from datetime import datetime
import time
import RPi.GPIO as GPIO

time.sleep(10)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=23                 # positive lead of buzzer goes to gpio 23 and negative to ground.
GPIO.setup(buzzer,GPIO.OUT)


for x in range(2):        # only plays during start up to confirm buzzer and code is running.
	for x in range(2):
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(0.05)
		GPIO.output(buzzer,GPIO.LOW)
		time.sleep(0.05)
	time.sleep(0.2)


def alarm():
	for x in range(10):
		for x in range(2):
			GPIO.output(buzzer,GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(buzzer,GPIO.LOW)
			time.sleep(0.1)
		time.sleep(0.5)
	time.sleep(51)

# set alarm here in this format:
# HHMM
# note: HH is 24hr
alarm1="0915"     # this is set for 9:15am
alarm2="1430"     # this is set for 2:30pm

#note: for 12am midnight, set HH to 00. same goes 
#      with MM, if you need 60 minutes, set to 00

while True:
	now=datetime.now()
	currentTime=now.strftime("%H%M")

	while currentTime==alarm1:
		alarm()
		break
	while currentTime==alarm2:
		alarm()
		break
	time.sleep(1)
		

