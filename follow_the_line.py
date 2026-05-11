import RPi.GPIO as GPIO
import time

PIN_TRIGGER = 23
PIN_ECHO = 24

ir_l = 20
ir_r = 26

e1 = 6
m1 = 12
e2 = 16
m2 = 19


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(ir_l, GPIO.IN)
GPIO.setup(ir_r, GPIO.IN)

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
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(60)
    enb.ChangeDutyCycle(60)


def backward():
    GPIO.output(m1,True)
    GPIO.output(m2,True)
    ena.ChangeDutyCycle(60)
    enb.ChangeDutyCycle(60)


def stop():
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(0)
    enb.ChangeDutyCycle(0)

def left():
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(0)
    enb.ChangeDutyCycle(60)

def right():
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(60)
    enb.ChangeDutyCycle(0)
    
def get_distance():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)


    time.sleep(2)


    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)

    return distance

while True:
    leftv = GPIO.input(ir_l)
    rightv = GPIO.input(ir_r)

    print(f"left{leftv}")
    print(f"right{rightv}")

    if leftv == 0 and rightv == 0:
        forward()
    elif leftv == 1 and rightv == 0:
        left()
    elif leftv == 0 and rightv == 1:
        right()
    elif leftv == 1 and rightv == 1:
        stop()
