
import RPi.GPIO as GPIO 
import time 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(23,GPIO.OUT)
#GPIO.setup(24,GPIO.OUT)
GPIO.output(23, GPIO.HIGH)
#GPIO.output(24, GPIO.LOW)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
GPIO.output(19, GPIO.LOW)
#time.sleep(4)
#GPIO.output(18, GPIO.HIGH)
#GPIO.output(19, GPIO.LOW)

#GPIO.cleanup()
