import RPi.GPIO as GPIO
import time
import os
from twilio.rest import Client
import subprocess

account_sid = 'AC5f8f463f802c9cb02a145a98029ed5da'
auth_token = 'a2d49a78ab160c26d1faea2a138f5aed'
client = Client(account_sid, auth_token)

GPIO.setmode(GPIO.BCM)
DO_PIN = 5 
GPIO.setup(DO_PIN, GPIO.IN)

try:
    while True:
        gas_present = GPIO.input(DO_PIN)

        if gas_present == GPIO.HIGH:
            gas_state = "Gas Present"
            call = client.calls.create(
              url="http://demo.twilio.com/docs/voice.xml",
              to='+355688008886',
              from_='+16057414265'
            )
            print(call.sid)
            break
        else:
            gas_state = "No Gas"

        print(f"Gas State: {gas_state}")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Gas detection stopped by user")

GPIO.cleanup()
subprocess.call(["/home/flatratedijes/lumen/venv/bin/python3", "/home/flatratedijes/lumen/lumen_m.py"])
