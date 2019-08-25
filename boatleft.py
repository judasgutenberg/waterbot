
import  RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24, GPIO.HIGH)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.output(12, GPIO.HIGH)
