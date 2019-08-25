
import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)

GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
