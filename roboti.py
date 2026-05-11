import RPi.GPIO as GPIO
import time


e1 = 6
m1 = 12
e2 = 19
m2 = 16


PIN_TRIGGER = 23
PIN_ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(e1, GPIO.OUT)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(e2, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)

GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

ena = GPIO.PWM(e1, 1000)
enb = GPIO.PWM(e2, 1000)
ena.start(0)
enb.start(0)

def forward():
    GPIO.output(m1,True)
    GPIO.output(m2,True)
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(100)


def backward():
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(100)

def stop():
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(0)
    enb.ChangeDutyCycle(0)

def left():
    GPIO.output(m1,False)
    GPIO.output(m2,True)
    ena.ChangeDutyCycle(0)
    enb.ChangeDutyCycle(100)

def right():
    GPIO.output(m1,True)
    GPIO.output(m2,False)
    enb.ChangeDutyCycle(0)
    ena.ChangeDutyCycle(100)


def get_distance():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    print( "Waiting for sensor to settle")
    time.sleep(2)
    print( "Calculating distance")
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance:",distance,"cm")

    return distance

while True:
    try:

        i = input()
        if i == 'f':
            forward()
            time.sleep(2)
        elif i == 'b':
            backward()
            time.sleep(2)
        elif i == 's':
            stop()
            time.sleep(2)
        elif i == 'l':
            left()
            time.sleep(2)
        elif i == 'r':
            right()
            time.sleep(2)

        elif i =="u":
            get_distance()
    except KeyboardInterrupt:
        print("DONE")
        break
