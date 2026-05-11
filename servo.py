import RPi.GPIO as GPIO
import time
import datetime
from espeak import espeak

servoPIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
espeak.synth("Stop, you will be conqured by robots")
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
while True:
    p.start(2.5) # Initialization
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
