import RPi.GPIO as GPIO
import time

PIN_TRIGGER = 23
PIN_ECHO = 24
servo_pin = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

pwm=GPIO.PWM(servo_pin, 50)
pwm.start(0)



def get_distance():
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(2)
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    
    pulse_start_time = 0
    pulse_end_time = 0
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print("Distance:",distance,"cm")

    return distance


leftp = 2.5
neutral = 7.5
rightp = 12
while True:
    print("begin test")

    print("duty cycle", leftp,"% at left -90 deg")
    left = get_distance()
    pwm.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    print("duty cycle", neutral,"% at 0 deg")
    center = get_distance()
    pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)

    print("duty cycle",rightp, "% at right +90 deg")
    right = get_distance()
    pwm.ChangeDutyCycle(12)
    time.sleep(0.5)
    
    print(f"left {left}")
    print(f"neutral {neutral}")
    print(f"center {center}")


pwm.stop()
GPIO.cleanup()
