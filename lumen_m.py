import RPi.GPIO as GPIO
import time
from gpiozero import DistanceSensor

PIN_TRIGGER = 23
PIN_ECHO = 24  

servo_pin = 11

ir_l = 20 
ir_r = 26
e1 = 6
m1 = 12
e2 = 16
m2 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(servo_pin, GPIO.OUT)


GPIO.setup(ir_l, GPIO.IN)
GPIO.setup(ir_r, GPIO.IN)

GPIO.setup(e1, GPIO.OUT)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(e2, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)

ena = GPIO.PWM(e1, 1000)
enb = GPIO.PWM(e2, 1000)
pwm=GPIO.PWM(servo_pin, 50)

ena.start(0)
enb.start(0)
pwm.start(7.5)

ultrasonic = DistanceSensor(echo=PIN_ECHO, trigger=PIN_TRIGGER)
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
    enb.ChangeDutyCycle(100)

def right():
    GPIO.output(m1,False)
    GPIO.output(m2,False)
    ena.ChangeDutyCycle(100)
    enb.ChangeDutyCycle(0)
    
def get_distance():
    distance = ultrasonic.distance
    return distance
    
def left_distance():
    print("duty cycle", 12,"% at left -90 deg")
    pwm.ChangeDutyCycle(12)
    time.sleep(1)
    l_distance = get_distance()
    return l_distance
    

def right_distance():
    print("duty cycle", 2.5,"% at right -90 deg")
    pwm.ChangeDutyCycle(2.5)
    time.sleep(1)
    r_distance = get_distance()
    return r_distance
    
leftp = 2.5
neutral = 7.5
rightp = 12

while True:
    if get_distance() >= 0.15:
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

    else:
        backward()
        time.sleep(1)
        stop()
	
        l_distance = left_distance()
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)

        r_distance = right_distance()
        pwm.ChangeDutyCycle(7.5)
        time.sleep(1)

        print(f"left {l_distance }")
        print(f"right {r_distance }")

        if max(l_distance , r_distance) == r_distance:
            right()
            time.sleep(1)
        elif max(l_distance , r_distance) == l_distance:
            left()
            time.sleep(1)

pwm.stop()
GPIO.cleanup()

