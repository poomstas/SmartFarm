import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAY_1_GPIO = 7
GPIO.setup(RELAY_1_GPIO, GPIO.OUT) # GPIO Assign mode

try:
    while True:
        print("Setting HIGH")
        GPIO.output(RELAY_1_GPIO, GPIO.HIGH) # on
        time.sleep(5)
        print("Setting LOW")
        GPIO.output(RELAY_1_GPIO, GPIO.LOW) # out
        time.sleep(5)
finally:
    GPIO.cleanup()