'''
Turn on the water pump, and alternate the fan switch in 5 second intervals.
This is to check if the power supplied to the water pump is affected by the fan turning on. 
'''

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Use GPIO Numbers instead of board numbers

# GPIO-7 is No2 (Fan), GPIO-8 is No1 (Water Pump)
GPIO_FAN, GPIO_PUMP = 7, 8
GPIO.setup(GPIO_FAN, GPIO.OUT)      # GPIO Assign mode
GPIO.setup(GPIO_PUMP, GPIO.OUT)     # GPIO Assign mode

GPIO.output(GPIO_FAN, GPIO.HIGH)    # GPIO.HIGH on a relay is OFF
GPIO.output(GPIO_PUMP, GPIO.HIGH)   # GPIO.HIGH on a relay is OFF
time.sleep(1)

try:
    GPIO.output(GPIO_PUMP, GPIO.LOW)
    while True:
        print("Setting No7 to LOW (Fan On)")
        GPIO.output(GPIO_FAN, GPIO.LOW)
        time.sleep(5)

        print("Setting No7 to HIGH (Fan Off)")
        GPIO.output(GPIO_FAN, GPIO.HIGH)
        time.sleep(5)
finally:
    GPIO.cleanup()