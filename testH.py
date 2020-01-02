
import RPi.GPIO as GPIO
from l298n import *
import time

engine = L298N(8, 10, 27, 29, 31, 33)

def drive():
    engine.driveForward()
    engine.setPulse(70)
    time.sleep(10)
    GPIO.cleanup()
try:
    drive()
except Exception as e:
    print e
    GPIO.cleanup()
    
